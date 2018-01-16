import math
import sys
import logging
from spinal_cord.frequency_generators.list_generator import FrequencyListGenerator

logger = logging.getLogger(__name__)


class TestGenerator(FrequencyListGenerator):
    def __init__(self):
        super().__init__()
        # this frequencies is used one by one while the frequency list is filling
        self.frequencies = [50, 100]
        logger.debug('Using frequencies: ' + str(self.frequencies))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

    assert len(sys.argv) == 3, '2 arguments needed simulation time and interval'
    testTime = int(sys.argv[1])
    testInterval = int(sys.argv[2])
    logger.info('Parameters (time, interval): ' + str(testTime) + ' ' + str(testInterval))

    testGenerator = TestGenerator()
    logger.debug('TestGenerator constructed')
    frequencyList = testGenerator.generate(testTime, testInterval)
    spikeList = frequencyList.generate_spikes()

    numberOfIntervals = testTime * 1000 // testInterval
    assert numberOfIntervals == len(frequencyList), 'frequency list size must be equal to the number of intervals'

    # storage for number of spikes per interval
    spikesPerInterval = [0] * numberOfIntervals

    # collecting number of spikes per interval
    for spikeTime in spikeList:
        spikeIndex = int(spikeTime / testInterval)
        spikesPerInterval[spikeIndex] += 1
    logger.info('Spikes per interval: ' + str(spikesPerInterval))

    # assert that number of spikes corresponds to their frequency
    acceptableErrorNumberOfSpikes = 2
    for i in range(numberOfIntervals):
        intervalFrequency = frequencyList.list[i] / numberOfIntervals * testTime
        assert math.fabs(intervalFrequency - spikesPerInterval[i]) < acceptableErrorNumberOfSpikes, \
            'number of spikes corresponds to their frequency'

    # assert that total number of spike corresponds to average frequency
    average_frequency = sum(frequencyList.list) / len(frequencyList)
    logger.debug('Expected number of spikes: ' + str(average_frequency * testTime))
    logger.debug('Actual number of spikes: ' + str(len(spikeList)))
    assert math.fabs(average_frequency * testTime - len(spikeList)) < acceptableErrorNumberOfSpikes, \
        'too much difference between expected and actual numbers of spikes'
