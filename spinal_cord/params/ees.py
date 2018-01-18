import numpy
from spinal_cord.network_items_names import EES


def generate_spike_times(frequency_hz, how_long_s):
    """
    :param frequency_hz: in Hertz
    :param how_long_s: in seconds
    :return: array of spike times
    """
    how_many = int(frequency_hz * how_long_s)
    start = 1000 // frequency_hz
    return numpy.linspace(start, how_long_s * 1000, how_many, dtype=numpy.int)


ees_params = dict()

ees_frequency = 40  # 40 is the optimal one
ees_duration = 1000  # we set it to be much longer than any possible simulation to generate enough spike times.
ees_amplitude = 500  # amplitude of ees current in uA. Range of values is (0, 600).
ees_params[EES.EES] = dict(
    model="spike_generator",
    n=1,
    params={'spike_times': generate_spike_times(ees_frequency, ees_duration).astype(float)},
)
