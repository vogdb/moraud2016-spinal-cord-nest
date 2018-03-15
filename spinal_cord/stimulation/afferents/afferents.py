import spinal_cord.stimulation.data_names as stimulation_names
import pkg_resources


class AfferentsFile:
    MAX_NUM = 60

    @staticmethod
    def get_rate_params(filepath, speed, interval, number, type, muscle):
        if number <= 0 or number > AfferentsFile.MAX_NUM:
            raise ValueError(
                "AfferentsFile.number must be greater than 0 and less or equal than {}".format(AfferentsFile.MAX_NUM)
            )

        with open(AfferentsFile._get_data_file(filepath, type, muscle, speed, interval), "r") as data_file:
            frequencies_list = []
            for line in data_file:
                frequency_list = [float(frequency) for frequency in line.strip().split()]
                frequencies_list.append(frequency_list)
                if len(frequencies_list) >= number:
                    break
        # rate_times must be equal for all records, so calculate them one time only
        rate_times = [float(time_step) for time_step in
                      range(0, interval.value * len(frequencies_list[0]), interval.value)]

        return [{'rate_times': rate_times, 'rate_values': frequency_list} for frequency_list in frequencies_list]

    @staticmethod
    def _get_data_file(filepath, type, muscle, speed, interval):
        # example: Ia_GM_speed15_int20.txt
        filename = type.value + "_" + muscle.value + "_speed" \
                   + str(speed.value) + "_int" + str(interval.value) + ".txt"
        return pkg_resources.resource_filename("spinal_cord", filepath + filename)


def test():
    flex_params_list = AfferentsFile.get_rate_params(
        '/stimulation/afferents/data/',
        stimulation_names.Speed.DEFAULT,
        stimulation_names.Interval.TWENTY,
        20,
        stimulation_names.NeuronTypes.ONE_A,
        stimulation_names.Muscles.FLEX
    )

    extens_params_list = AfferentsFile.get_rate_params(
        '/stimulation/afferents/data/',
        stimulation_names.Speed.DEFAULT,
        stimulation_names.Interval.TWENTY,
        20,
        stimulation_names.NeuronTypes.ONE_A,
        stimulation_names.Muscles.FLEX
    )

    for extens_params in extens_params_list:
        print(extens_params)
        assert len(extens_params['rate_times']) == len(extens_params['rate_values'])
    for flex_params in flex_params_list:
        print(flex_params)
        assert len(flex_params['rate_times']) == len(flex_params['rate_values'])

# test()
