import logging
import re

logger = logging.getLogger(__name__)


class FrequencyList:
    """
    List of frequencies at given time interval.

    Attributes:
        interval (int): In milliseconds. Time interval between frequencies.
        list (:obj:`list` of :obj:`int`): list of frequencies.
        name (str, optional): Name of the list.

    """

    def __init__(self, interval, list, name=''):
        self.interval = interval
        self.list = list
        self.name = name

    def __len__(self):
        return len(self.list)

    def generate_spikes(self):
        """
        Generates a list of spikes by using its own frequency list.

        Returns:
            list: the list of spike times

        """

        logger.info('Spike generation started')
        logger.debug('Using frequency list: ' + str(self.list))
        spike_times = []
        # initial time
        time = 0.0
        charge = 0.0
        for frequency in self.list:
            spikes_at_interval = int(self.interval / 1000 * frequency)

            charge += self.interval / 1000 * frequency - spikes_at_interval
            if charge > 1:
                charge -= 1
                spikes_at_interval += 1

            if spikes_at_interval > 0:
                time_between_spikes = self.interval / spikes_at_interval
                time -= time_between_spikes / 2  # shifting time to place spikes closer to the center
                spike_times.extend(
                    [round(time + time_between_spikes * (n + 1), 1) for n in range(spikes_at_interval)])
                time += time_between_spikes / 2  # shifting back
            time += self.interval
        logger.info('Spike generation finished')
        logger.debug('Spike times: ' + str(spike_times))
        logger.debug('Total spikes generated: ' + str(len(spike_times)))
        return spike_times


class FrequencyListFile(FrequencyList):
    """
    List of frequencies at given time interval.
    Receives data from a specific file.
    The filename has to contain a word 'interval' and an integer number after it where
    the number is a value of the interval in ms.
    If several intervals mentioned then the first one will be used

    If there are several lines in the file then the first one will be read

    Attributes:
        filename (str): The name of the file with frequency data
        name (str, optional): Name of the list.

    """

    def __init__(self, filename, name=''):
        f = open(filename, mode='r')
        interval = int(re.search('interval(?P<interval>[\d]+)', filename, flags=re.IGNORECASE).group('interval'))
        frequency_list = [float(value) for value in f.readline().split()]
        f.close()
        super().__init__(interval=interval, list=frequency_list, name=name)
