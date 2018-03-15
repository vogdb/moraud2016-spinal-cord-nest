from spinal_cord.network_items_names import NeuronGroups, Afferents
from spinal_cord.params.afferents import afferent_params

neuron_group_params = dict()

inter_model_params = {
    'tau_m': 30.0,
    'tau_syn_ex': 0.5,
    'tau_syn_in_rise': 5.0,
    'tau_syn_in_fall': 10.0,
    't_ref': 1.0,
}
inter_model_number = 196
inter_model_type = 'int_fire4'

neuron_group_params[NeuronGroups.FLEX_INTER_1A] = dict(
    model=inter_model_type,
    params=inter_model_params,
    n=inter_model_number,
)

neuron_group_params[NeuronGroups.EXTENS_INTER_1A] = dict(
    model=inter_model_type,
    params=inter_model_params,
    n=inter_model_number,
)

neuron_group_params[NeuronGroups.FLEX_INTER_2] = dict(
    model=inter_model_type,
    params=inter_model_params,
    n=inter_model_number,
)

neuron_group_params[NeuronGroups.EXTENS_INTER_2] = dict(
    model=inter_model_type,
    params=inter_model_params,
    n=inter_model_number,
)

motor_model_params = {
    'tau_syn_ex': 0.5,
    'tau_syn_in': 1.5,
    't_ref': 2.0,
    #'g_K_Ca_5ht': 0.4,
}
motor_model_number = 169
motor_model_type = 'hh_moto_5ht'

neuron_group_params[NeuronGroups.EXTENS_MOTOR] = dict(
    model=motor_model_type,
    params=motor_model_params,
    n=motor_model_number,
)
neuron_group_params[NeuronGroups.FLEX_MOTOR] = dict(
    model=motor_model_type,
    params=motor_model_params,
    n=motor_model_number,
)

# Dummy neuron groups for afferents simulation
afferent_model_params = {
    'tau': 0.5,
    't_ref': 1.0,
}
afferent_model_type = 'int_fire1'

neuron_group_params[NeuronGroups.FLEX_AFFERENT_1A] = dict(
    model=afferent_model_type,
    params=afferent_model_params,
    n=afferent_params[Afferents.FLEX_1A]['n'],
)

neuron_group_params[NeuronGroups.EXTENS_AFFERENT_1A] = dict(
    model=afferent_model_type,
    params=afferent_model_params,
    n=afferent_params[Afferents.EXTENS_1A]['n'],
)

neuron_group_params[NeuronGroups.FLEX_AFFERENT_2] = dict(
    model=afferent_model_type,
    params=afferent_model_params,
    n=afferent_params[Afferents.FLEX_2]['n'],
)

neuron_group_params[NeuronGroups.EXTENS_AFFERENT_2] = dict(
    model=afferent_model_type,
    params=afferent_model_params,
    n=afferent_params[Afferents.EXTENS_2]['n'],
)
