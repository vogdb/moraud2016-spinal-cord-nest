import pylab
import numpy as np

import definitions
from spinal_cord import device_data
from spinal_cord.network_items_names import Multimeters, SpikeDetectors
import spinal_cord.params as spinal_cord_params
from spinal_cord.device_plot import MultimeterPlot, SpikeDetectorPlot

multimeter_plot = MultimeterPlot(5, 'Average "V_m" of neuron groups')
spike_detector_plot = SpikeDetectorPlot(5, 'Spike plots')


def plot_multimeter(flexor_device, extensor_device, group_name):
    flexor_data = device_data.get_average_voltage(
        flexor_device,
        definitions.RESULTS_DIR
    )
    extensor_data = device_data.get_average_voltage(
        extensor_device,
        definitions.RESULTS_DIR
    )
    multimeter_plot.subplot(flexor_data, extensor_data, group_name)


def plot_spike_detector(flexor_device, extensor_device, group_name, group_num):
    flexor_data = device_data.extract_spike_detector_data(
        flexor_device,
        definitions.RESULTS_DIR
    )
    extensor_data = device_data.extract_spike_detector_data(
        extensor_device,
        definitions.RESULTS_DIR
    )
    id_offset = 0
    if len(flexor_data['neuron_id']) > 0:
        id_offset = flexor_data['neuron_id'][0] - extensor_data['neuron_id'][0] + group_num
    flexor_data['neuron_id'] = np.array(flexor_data['neuron_id']) - id_offset

    spike_detector_plot.subplot(flexor_data, extensor_data, group_name)


def display_results():
    multimeter_plot.reset()
    plot_multimeter(Multimeters.FLEX_MOTOR, Multimeters.EXTENS_MOTOR, 'Motor')
    plot_multimeter(Multimeters.FLEX_INTER_1A, Multimeters.EXTENS_INTER_1A, 'Inter1A')
    plot_multimeter(Multimeters.FLEX_INTER_2, Multimeters.EXTENS_INTER_2, 'Inter2')
    plot_multimeter(Multimeters.FLEX_AFFERENT_1A, Multimeters.EXTENS_AFFERENT_1A, 'Afferent1A')
    plot_multimeter(Multimeters.FLEX_AFFERENT_2, Multimeters.EXTENS_AFFERENT_2, 'Afferent2')

    spike_detector_plot.reset()
    plot_spike_detector(SpikeDetectors.FLEX_MOTOR, SpikeDetectors.EXTENS_MOTOR, 'Motor',
                        spinal_cord_params.neuron_groups.motor_model_number)
    plot_spike_detector(SpikeDetectors.FLEX_INTER_1A, SpikeDetectors.EXTENS_INTER_1A, 'Inter1A',
                        spinal_cord_params.neuron_groups.inter_model_number)
    plot_spike_detector(SpikeDetectors.FLEX_INTER_2, SpikeDetectors.EXTENS_INTER_2, 'Inter2',
                        spinal_cord_params.neuron_groups.inter_model_number)
    plot_spike_detector(SpikeDetectors.FLEX_AFFERENT_1A, SpikeDetectors.EXTENS_AFFERENT_1A, 'Afferent1A',
                        spinal_cord_params.afferents.generator_number_1a)
    plot_spike_detector(SpikeDetectors.FLEX_AFFERENT_2, SpikeDetectors.EXTENS_AFFERENT_2, 'Afferent1A',
                        spinal_cord_params.afferents.generator_number_2)

    pylab.show()
