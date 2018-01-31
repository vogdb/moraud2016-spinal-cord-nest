import spinal_cord.stimulation.data_names as stimulation_names
import spinal_cord.stimulation.afferents.afferents as afferents
from spinal_cord.network_items_names import Afferents, NeuronGroups

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

# TODO parameters below should be as in Neuron Simulator 'IntFire1' with tau = 0.5, refrac = 1
inter_model_params = {
    'V_m': 0.0,
    'V_reset': 0.0,
    'V_th': 1.0,
    'tau_m': 0.5,
    'tau_syn_ex': 0.1,
    't_ref': 1.0,
}
inter_model_type = 'iaf_psc_alpha'

afferent_params[NeuronGroups.FLEX_AFFERENT_1A] = dict(
    model=inter_model_type,
    params=inter_model_params,
    n=generator_number_1a,
)

afferent_params[NeuronGroups.EXTENS_AFFERENT_1A] = dict(
    model=inter_model_type,
    params=inter_model_params,
    n=generator_number_1a,
)

afferent_params[NeuronGroups.FLEX_AFFERENT_2] = dict(
    model=inter_model_type,
    params=inter_model_params,
    n=generator_number_2,
)

afferent_params[NeuronGroups.EXTENS_AFFERENT_2] = dict(
    model=inter_model_type,
    params=inter_model_params,
    n=generator_number_2,
)
