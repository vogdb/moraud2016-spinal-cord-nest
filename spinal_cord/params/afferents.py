import spinal_cord.stimulation.data_names as stimulation_names
import spinal_cord.stimulation.afferents.afferents as afferents
from spinal_cord.network_items_names import Afferents

afferent_params = dict()

afferent_filepath = "/stimulation/afferents/data/"
generator_number_1a = afferents.AfferentsFile.MAX_NUM

afferent_params[Afferents.FLEX_1A] = dict(
    model="inhomogeneous_poisson_generator",
    n=generator_number_1a,
    params=afferents.AfferentsFile.get_rate_params(
        filepath=afferent_filepath,
        speed=stimulation_names.Speed.FIFTEEN,
        interval=stimulation_names.Interval.TWENTY,
        type=stimulation_names.NeuronTypes.ONE_A,
        muscle=stimulation_names.Muscles.FLEX,
        number=generator_number_1a,
    ),
)
afferent_params[Afferents.EXTENS_1A] = dict(
    model="inhomogeneous_poisson_generator",
    n=generator_number_1a,
    params=afferents.AfferentsFile.get_rate_params(
        filepath=afferent_filepath,
        speed=stimulation_names.Speed.FIFTEEN,
        interval=stimulation_names.Interval.TWENTY,
        type=stimulation_names.NeuronTypes.ONE_A,
        muscle=stimulation_names.Muscles.EXTENS,
        number=generator_number_1a,
    ),
)

generator_number_2 = afferents.AfferentsFile.MAX_NUM
afferent_params[Afferents.FLEX_2] = dict(
    model="inhomogeneous_poisson_generator",
    n=generator_number_2,
    params=afferents.AfferentsFile.get_rate_params(
        filepath=afferent_filepath,
        speed=stimulation_names.Speed.FIFTEEN,
        interval=stimulation_names.Interval.TWENTY,
        type=stimulation_names.NeuronTypes.TWO,
        muscle=stimulation_names.Muscles.FLEX,
        number=generator_number_2,
    ),
)
afferent_params[Afferents.EXTENS_2] = dict(
    model="inhomogeneous_poisson_generator",
    n=generator_number_2,
    params=afferents.AfferentsFile.get_rate_params(
        filepath=afferent_filepath,
        speed=stimulation_names.Speed.FIFTEEN,
        interval=stimulation_names.Interval.TWENTY,
        type=stimulation_names.NeuronTypes.TWO,
        muscle=stimulation_names.Muscles.EXTENS,
        number=generator_number_2,
    ),
)
