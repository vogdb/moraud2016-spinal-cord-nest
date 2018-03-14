import nest

import definitions
from spinal_cord import device_data
from spinal_cord import util
from spinal_cord.network_items_names import Multimeters
from spinal_cord.neuron_network import NeuronNetwork
from spinal_cord.params.afferents import afferent_params
from spinal_cord.params.connections import connection_params_list
from spinal_cord.params.devices import device_params
from spinal_cord.params.neuron_groups import neuron_group_params
from spinal_cord.params.ees import ees_params
from spinal_cord.results_plotter import ResultsPlotter


def plot_neuron_group(flexor_device, extensor_device, group_name):
    flexor_motor_data = device_data.get_average_voltage(
        flexor_device,
        definitions.RESULTS_DIR
    )
    extensor_motor_data = device_data.get_average_voltage(
        extensor_device,
        definitions.RESULTS_DIR
    )
    plotter.subplot(flexor_motor_data, extensor_motor_data, group_name)


nest.Install("research_team_models")
nest.Install("neuron_simulator_models")

entity_params = dict()
entity_params.update(afferent_params)
entity_params.update(neuron_group_params)
entity_params.update(device_params)
entity_params.update(ees_params)

util.clean_previous_results()
layer1 = NeuronNetwork(entity_params, connection_params_list)

nest.Simulate(150.)

plotter = ResultsPlotter(3, 'Average "V_m" of neuron groups')
plotter.reset()
plot_neuron_group(Multimeters.FLEX_MOTOR, Multimeters.EXTENS_MOTOR, 'Motor')
plot_neuron_group(Multimeters.FLEX_INTER_2, Multimeters.EXTENS_INTER_2, 'Inter2')
plot_neuron_group(Multimeters.FLEX_INTER_1A, Multimeters.EXTENS_INTER_1A, 'Inter1A')
plotter.show()
