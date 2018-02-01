import numpy
import pkg_resources


class EesStimulation:
    @staticmethod
    def compute_activated_number(amplitude, muscle, neuron_type, number):
        percent = EesStimulation.compute_activated_percent(amplitude, muscle, neuron_type)
        return int(round(number * percent))

    @staticmethod
    def compute_activated_percent(amplitude, muscle, neuron_type):
        if amplitude < 0 or amplitude > 600:
            raise ValueError('EES.compute_activated_percent(amplitude) param must be between 600 and 0')
        ruler_file = EesStimulation.get_ruler_file(muscle, neuron_type)
        ruler = numpy.loadtxt(ruler_file)
        available_currents = numpy.linspace(0, 600, 20)
        currents_delta = abs(available_currents - amplitude)
        closest_computed_current_index = currents_delta.argmin()
        percent = ruler[closest_computed_current_index] / max(ruler)
        return percent

    @staticmethod
    def get_ruler_file(muscle, neuron_type):
        filename = muscle.value + '_full_' + neuron_type.value + '_S1_wire1'
        filepath = '/stimulation/ees/data/'
        return pkg_resources.resource_filename("spinal_cord", filepath + filename)


def test():
    import spinal_cord.stimulation.data_names as data_names
    print(EesStimulation.compute_activated_percent(300, data_names.Muscles.FLEX, data_names.NeuronTypes.ONE_A))
    print(EesStimulation.compute_activated_percent(300, data_names.Muscles.FLEX, data_names.NeuronTypes.TWO))
    print(EesStimulation.compute_activated_percent(300, data_names.Muscles.FLEX, data_names.NeuronTypes.MOTO))
    print(EesStimulation.compute_activated_percent(300, data_names.Muscles.EXTENS, data_names.NeuronTypes.ONE_A))
    print(EesStimulation.compute_activated_percent(300, data_names.Muscles.EXTENS, data_names.NeuronTypes.TWO))
    print(EesStimulation.compute_activated_percent(300, data_names.Muscles.EXTENS, data_names.NeuronTypes.MOTO))

# test()
