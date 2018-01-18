import spinal_cord.stimulation.data_names as stimulation_names
import spinal_cord.stimulation.afferents.afferents as afferents
from spinal_cord.network_items_names import Afferents

afferent_params = dict()

afferent_filepath = "/stimulation/afferents/data/"
generator_number_1a = 60

afferent_params[Afferents.FLEX_1A] = dict(
    model="spike_generator",
    n=generator_number_1a,
    params=afferents.AfferentsFile.get_nest_spike_times(
        filepath=afferent_filepath,
        speed=stimulation_names.Speed.FIFTEEN,
        interval=stimulation_names.Interval.TWENTY,
        type=stimulation_names.NeuronTypes.ONE_A,
        muscle=stimulation_names.Muscles.FLEX,
        number=generator_number_1a,
    ),
)
afferent_params[Afferents.EXTENS_1A] = dict(
    model="spike_generator",
    n=generator_number_1a,
    params=afferents.AfferentsFile.get_nest_spike_times(
        filepath=afferent_filepath,
        speed=stimulation_names.Speed.FIFTEEN,
        interval=stimulation_names.Interval.TWENTY,
        type=stimulation_names.NeuronTypes.ONE_A,
        muscle=stimulation_names.Muscles.EXTENS,
        number=generator_number_1a,
    ),
)

generator_number_2 = 60
afferent_params[Afferents.FLEX_2] = dict(
    model="spike_generator",
    n=generator_number_2,
    params=afferents.AfferentsFile.get_nest_spike_times(
        filepath=afferent_filepath,
        speed=stimulation_names.Speed.FIFTEEN,
        interval=stimulation_names.Interval.TWENTY,
        type=stimulation_names.NeuronTypes.TWO,
        muscle=stimulation_names.Muscles.FLEX,
        number=generator_number_2,
    ),
)
afferent_params[Afferents.EXTENS_2] = dict(
    model="spike_generator",
    n=generator_number_2,
    params=afferents.AfferentsFile.get_nest_spike_times(
        filepath=afferent_filepath,
        speed=stimulation_names.Speed.FIFTEEN,
        interval=stimulation_names.Interval.TWENTY,
        type=stimulation_names.NeuronTypes.TWO,
        muscle=stimulation_names.Muscles.EXTENS,
        number=generator_number_2,
    ),
)
