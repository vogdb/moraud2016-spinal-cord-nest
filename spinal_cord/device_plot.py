import pylab as pylab


class PairPlot(object):
    def __init__(self, rows_number, title):
        self._rows_number = rows_number
        self._cols_number = 1
        self._plot_index = 1
        self._title = title

    def reset(self):
        pylab.figure(self._title)
        pylab.suptitle(self._title)

    def _subplot(self, title):
        if self._plot_index > self._rows_number:
            raise ValueError("Too many subplots!")
        pylab.subplot(self._rows_number, self._cols_number, self._plot_index)
        self._plot_index += 1
        pylab.ylabel(title)


class MultimeterPlot(PairPlot):
    def subplot(self, flexor, extensor, title):
        self._subplot(title)

        pylab.plot(flexor.keys(), flexor.values(), 'r.', label='flexor')
        pylab.plot(extensor.keys(), extensor.values(), 'b-.', label='extensor')

        pylab.legend()


class SpikeDetectorPlot(PairPlot):
    def subplot(self, flexor, extensor, title):
        self._subplot(title)

        pylab.plot(extensor['timestamp'], extensor['neuron_id'], 'b.', label='extensor', alpha=0.5)
        pylab.plot(flexor['timestamp'], flexor['neuron_id'], 'r.', label='flexor', alpha=0.5)

        pylab.legend()
