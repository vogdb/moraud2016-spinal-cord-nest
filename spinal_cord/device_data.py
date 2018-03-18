import os
from collections import OrderedDict


class MultimeterData:
    """
    format of _items: dict(<simulation_time>: dict(<neuron_id>: <list of recorder values>))
    """

    def __init__(self, recorded_params) -> None:
        self._items = OrderedDict()
        self._recorded_params = recorded_params

    def add_item(self, time, neuron_id, value_list):
        if not self.has_item(time):
            self.create_item(time)
        item = self.get_item(time)
        if neuron_id in item:
            raise ValueError("MultimeterData data item " + time + " already has neuron_id " + neuron_id)
        item[neuron_id] = value_list

    def has_item(self, time):
        return time in self._items

    def get_item(self, time):
        return self._items[time]

    def create_item(self, time):
        self._items[time] = dict()

    def get_data(self):
        return self._items

    def get_data_for_single_neuron(self, neuron_id, items):
        return self.get_data_for_neurons([neuron_id], items)

    def get_data_for_neurons(self, neuron_id_list, items=None):
        result = OrderedDict()
        if items is None:
            items = self._items
        for time, item in items.items():
            item_for_neurons = {neuron_id: values for neuron_id, values in item.items() if neuron_id in neuron_id_list}
            result[time] = item_for_neurons
        return result

    def filter_items_for_value(self, value_name, items=None):
        result = OrderedDict()
        data_index = self._recorded_params.index(value_name)
        if data_index is not None:
            if items is None:
                items = self._items
            for time, item in items.items():
                item = {neuron_id: values[data_index] for neuron_id, values in item.items()}
                result[time] = item
        return result

    def average(self, value_name):
        result = OrderedDict()
        for time, item in self.filter_items_for_value(value_name).items():
            values_list = item.values()
            average_value = round(sum(values_list) / float(len(values_list)), 3)
            result[time] = average_value
        return result


def get_device_filepath(device_name, storage_dir):
    device_filepath = None
    for file in os.listdir(storage_dir):
        if file.startswith(device_name.value):
            device_filepath = storage_dir + '/' + file
            break
    return device_filepath


def extract_multimeter_data(device_name, recorded_params, storage_dir):
    device_filepath = get_device_filepath(device_name, storage_dir)

    if device_filepath is not None:
        data = MultimeterData(recorded_params)
        with open(device_filepath) as device_file:
            for line in device_file:
                line = line.split()
                time = float(line[1])
                neuron_id = int(line[0])
                values = [float(value) for value in line[2:]]
                data.add_item(time, neuron_id, values)
        return data
    return None


def extract_spike_detector_data(device_name, storage_dir):
    device_filepath = get_device_filepath(device_name, storage_dir)
    if device_filepath is not None:
        data = {'timestamp': [], 'neuron_id': []}
        with open(device_filepath) as device_file:
            for line in device_file:
                line = line.split()
                time = float(line[1])
                neuron_id = int(line[0])
                data['timestamp'].append(time)
                data['neuron_id'].append(neuron_id)
        return data
    return None



def get_average_voltage(device_name, storage_dir):
    data = extract_multimeter_data(
        device_name,
        ['V_m'],
        storage_dir
    )
    return data.average('V_m')
