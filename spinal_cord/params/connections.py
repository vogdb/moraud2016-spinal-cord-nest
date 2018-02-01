from spinal_cord.network_items_names import NeuronGroups, Afferents, Multimeters, EES
import spinal_cord.params.ees as ees_params
from spinal_cord.params.neuron_groups import neuron_group_params
from spinal_cord.params.afferents import afferent_params
from spinal_cord.stimulation.ees.ees import EesStimulation
import spinal_cord.stimulation.data_names as stimulation_names

distr_normal_2 = {'distribution': 'normal', 'mu': 2.0, 'sigma': 0.175}  # 0.175^2 = 0.03
distr_normal_3 = {'distribution': 'normal', 'mu': 3.0, 'sigma': 0.175}  # 0.175^2 = 0.03
syn_default_model = 'static_synapse'

conn_all_to_all = {
    'rule': 'all_to_all'
}

syn_spec_afferent_artificial_neuron = {
    'model': syn_default_model,
    'delay': 1,
    'weight': 1  # spike from afferent should generate spike on its artificial representation
}
syn_spec_afferent1a_motor = {
    'model': syn_default_model,
    'delay': distr_normal_2,
    'weight': 0.052608
}
syn_spec_afferent1a_inter1a = {
    'model': syn_default_model,
    'delay': distr_normal_2,
    'weight': 0.0175
}
syn_spec_afferent2_inter2 = {
    'model': syn_default_model,
    'delay': distr_normal_3,
    'weight': 0.0175
}
syn_spec_afferent2_inter1a = syn_spec_afferent2_inter2
syn_spec_inter2_motor = {
    'model': syn_default_model,
    'delay': 1,
    'weight': 0.00907
}
syn_spec_inter1a_inter1a = {
    'model': syn_default_model,
    'delay': 1,
    'weight': -0.007
}
syn_spec_inter1a_motor = {
    'model': syn_default_model,
    'delay': 1,
    'weight': -0.0023
}

conn_spec_afferent_artificial_neuron = {
    'rule': 'one_to_one'
}
conn_spec_afferent1a_motor = conn_all_to_all
conn_spec_afferent1a_inter1a = {
    'rule': 'fixed_indegree',
    'indegree': 62,
}
conn_spec_afferent2_inter2 = {
    'rule': 'fixed_indegree',
    'indegree': 62,
}
conn_spec_afferent2_inter1a = conn_spec_afferent2_inter2
conn_spec_inter2_motor = {
    'rule': 'fixed_indegree',
    'indegree': 116,
}
conn_spec_inter1a_inter1a = {
    'rule': 'fixed_indegree',
    'indegree': 100,
}
conn_spec_inter1a_motor = {
    'rule': 'fixed_indegree',
    'indegree': 232,
}

connection_params_list = []

######## EES SOURCES #########
# EES - Motor
# syn_.tau = 0.1 syn_.e = 50
syn_spec_ees_motor = {
    'model': syn_default_model,
    'delay': 1,
    'weight': 20
}
ees_flex_motor_number = EesStimulation.compute_activated_number(
    ees_params.ees_amplitude,
    stimulation_names.Muscles.FLEX,
    stimulation_names.NeuronTypes.MOTO,
    neuron_group_params[NeuronGroups.FLEX_MOTOR]['n']
)
ees_extens_motor_number = EesStimulation.compute_activated_number(
    ees_params.ees_amplitude,
    stimulation_names.Muscles.EXTENS,
    stimulation_names.NeuronTypes.MOTO,
    neuron_group_params[NeuronGroups.EXTENS_MOTOR]['n']
)
connection_params_list.append(
    dict(
        pre=EES.EES,
        post=NeuronGroups.FLEX_MOTOR,
        syn_spec=syn_spec_ees_motor,
        conn_spec={'rule': 'fixed_indegree','indegree': ees_flex_motor_number},
    )
)
connection_params_list.append(
    dict(
        pre=EES.EES,
        post=NeuronGroups.EXTENS_MOTOR,
        syn_spec=syn_spec_ees_motor,
        conn_spec={'rule': 'fixed_indegree','indegree': ees_extens_motor_number},
    )
)

# EES - Afferents 1A
syn_spec_ees_afferent1a = {
    'model': syn_default_model,
    'delay': 1,
    'weight': 10
}
ees_flex_afferent1a_number = EesStimulation.compute_activated_number(
    ees_params.ees_amplitude,
    stimulation_names.Muscles.FLEX,
    stimulation_names.NeuronTypes.ONE_A,
    afferent_params[NeuronGroups.FLEX_AFFERENT_1A]['n']
)
ees_extens_afferent1a_number = EesStimulation.compute_activated_number(
    ees_params.ees_amplitude,
    stimulation_names.Muscles.EXTENS,
    stimulation_names.NeuronTypes.ONE_A,
    afferent_params[NeuronGroups.EXTENS_AFFERENT_1A]['n']
)
connection_params_list.append(
    dict(
        pre=EES.EES,
        post=NeuronGroups.FLEX_AFFERENT_1A,
        syn_spec=syn_spec_ees_afferent1a,
        conn_spec={'rule': 'fixed_indegree', 'indegree': ees_flex_afferent1a_number}
    )
)
connection_params_list.append(
    dict(
        pre=EES.EES,
        post=NeuronGroups.EXTENS_AFFERENT_1A,
        syn_spec=syn_spec_ees_afferent1a,
        conn_spec={'rule': 'fixed_indegree', 'indegree': ees_extens_afferent1a_number}
    )
)

# EES - Afferents 2
syn_spec_ees_afferent2 = {
    'model': syn_default_model,
    'delay': 1,
    'weight': 10
}
ees_flex_afferent2_number = EesStimulation.compute_activated_number(
    ees_params.ees_amplitude,
    stimulation_names.Muscles.FLEX,
    stimulation_names.NeuronTypes.TWO,
    afferent_params[NeuronGroups.FLEX_AFFERENT_2]['n']
)
ees_extens_afferent2_number = EesStimulation.compute_activated_number(
    ees_params.ees_amplitude,
    stimulation_names.Muscles.EXTENS,
    stimulation_names.NeuronTypes.TWO,
    afferent_params[NeuronGroups.EXTENS_AFFERENT_2]['n']
)
connection_params_list.append(
    dict(
        pre=EES.EES,
        post=NeuronGroups.FLEX_AFFERENT_2,
        syn_spec=syn_spec_ees_afferent2,
        conn_spec={'rule': 'fixed_indegree','indegree': ees_flex_afferent2_number}
    )
)
connection_params_list.append(
    dict(
        pre=EES.EES,
        post=NeuronGroups.EXTENS_AFFERENT_2,
        syn_spec=syn_spec_ees_afferent2,
        conn_spec={'rule': 'fixed_indegree','indegree': ees_extens_afferent2_number}
    )
)

######## FLEX SOURCES #########
# source is Afferents.FLEX_1A,
connection_params_list.append(
    dict(
        pre=Afferents.FLEX_1A,
        post=NeuronGroups.FLEX_AFFERENT_1A,
        syn_spec=syn_spec_afferent_artificial_neuron,
        conn_spec=conn_spec_afferent_artificial_neuron,
    )
)

# source is NeuronGroups.FLEX_AFFERENT_1A,
connection_params_list.append(
    dict(
        pre=NeuronGroups.FLEX_AFFERENT_1A,
        post=NeuronGroups.FLEX_MOTOR,
        syn_spec=syn_spec_afferent1a_motor,
        conn_spec=conn_spec_afferent1a_motor,
    )
)
connection_params_list.append(
    dict(
        pre=NeuronGroups.FLEX_AFFERENT_1A,
        post=NeuronGroups.FLEX_INTER_1A,
        syn_spec=syn_spec_afferent1a_inter1a,
        conn_spec=conn_spec_afferent1a_inter1a,
    )
)

# source is Afferents.FLEX_2
connection_params_list.append(
    dict(
        pre=Afferents.FLEX_2,
        post=NeuronGroups.FLEX_AFFERENT_2,
        syn_spec=syn_spec_afferent_artificial_neuron,
        conn_spec=conn_spec_afferent_artificial_neuron,
    )
)

# source is NeuronGroups.FLEX_AFFERENT_2,
connection_params_list.append(
    dict(
        pre=NeuronGroups.FLEX_AFFERENT_2,
        post=NeuronGroups.FLEX_INTER_2,
        syn_spec=syn_spec_afferent2_inter2,
        conn_spec=conn_spec_afferent2_inter2,
    )
)
connection_params_list.append(
    dict(
        pre=NeuronGroups.FLEX_AFFERENT_2,
        post=NeuronGroups.FLEX_INTER_1A,
        syn_spec=syn_spec_afferent2_inter1a,
        conn_spec=conn_spec_afferent2_inter1a,
    )
)

# source is NeuronGroups.FLEX_INTER_2
connection_params_list.append(
    dict(
        pre=NeuronGroups.FLEX_INTER_2,
        post=NeuronGroups.FLEX_MOTOR,
        syn_spec=syn_spec_inter2_motor,
        conn_spec=conn_spec_inter2_motor,
    )
)

# source is NeuronGroups.FLEX_INTER_1A
connection_params_list.append(
    dict(
        pre=NeuronGroups.FLEX_INTER_1A,
        post=NeuronGroups.EXTENS_INTER_1A,
        syn_spec=syn_spec_inter1a_inter1a,
        conn_spec=conn_spec_inter1a_inter1a,
    )
)
connection_params_list.append(
    dict(
        pre=NeuronGroups.FLEX_INTER_1A,
        post=NeuronGroups.EXTENS_MOTOR,
        syn_spec=syn_spec_inter1a_motor,
        conn_spec=conn_spec_inter1a_motor,
    )
)

######## EXTENSOR SOURCES #########
# source is Afferents.EXTENS_1A,
connection_params_list.append(
    dict(
        pre=Afferents.EXTENS_1A,
        post=NeuronGroups.EXTENS_AFFERENT_1A,
        syn_spec=syn_spec_afferent_artificial_neuron,
        conn_spec=conn_spec_afferent_artificial_neuron,
    )
)

# source is NeuronGroups.EXTENS_AFFERENT_1A,
connection_params_list.append(
    dict(
        pre=NeuronGroups.EXTENS_AFFERENT_1A,
        post=NeuronGroups.EXTENS_MOTOR,
        syn_spec=syn_spec_afferent1a_motor,
        conn_spec=conn_spec_afferent1a_motor,
    )
)
connection_params_list.append(
    dict(
        pre=NeuronGroups.EXTENS_AFFERENT_1A,
        post=NeuronGroups.EXTENS_INTER_1A,
        syn_spec=syn_spec_afferent1a_inter1a,
        conn_spec=conn_spec_afferent1a_inter1a,
    )
)

# source is Afferents.EXTENS_2
connection_params_list.append(
    dict(
        pre=Afferents.EXTENS_2,
        post=NeuronGroups.EXTENS_AFFERENT_2,
        syn_spec=syn_spec_afferent_artificial_neuron,
        conn_spec=conn_spec_afferent_artificial_neuron,
    )
)

# source is NeuronGroups.EXTENS_AFFERENT_2,
connection_params_list.append(
    dict(
        pre=NeuronGroups.EXTENS_AFFERENT_2,
        post=NeuronGroups.EXTENS_INTER_2,
        syn_spec=syn_spec_afferent2_inter2,
        conn_spec=conn_spec_afferent2_inter2,
    )
)
connection_params_list.append(
    dict(
        pre=NeuronGroups.EXTENS_AFFERENT_2,
        post=NeuronGroups.EXTENS_INTER_1A,
        syn_spec=syn_spec_afferent2_inter1a,
        conn_spec=conn_spec_afferent2_inter1a,
    )
)

# source is NeuronGroups.EXTENS_INTER_2
connection_params_list.append(
    dict(
        pre=NeuronGroups.EXTENS_INTER_2,
        post=NeuronGroups.EXTENS_MOTOR,
        syn_spec=syn_spec_inter2_motor,
        conn_spec=conn_spec_inter2_motor,
    )
)

# source is NeuronGroups.EXTENS_INTER_1A
connection_params_list.append(
    dict(
        pre=NeuronGroups.EXTENS_INTER_1A,
        post=NeuronGroups.FLEX_INTER_1A,
        syn_spec=syn_spec_inter1a_inter1a,
        conn_spec=conn_spec_inter1a_inter1a,
    )
)
connection_params_list.append(
    dict(
        pre=NeuronGroups.EXTENS_INTER_1A,
        post=NeuronGroups.FLEX_MOTOR,
        syn_spec=syn_spec_inter1a_motor,
        conn_spec=conn_spec_inter1a_motor,
    )
)

########## Devices ########
connection_params_list.append(
    dict(
        pre=Multimeters.FLEX_INTER_1A,
        post=NeuronGroups.FLEX_INTER_1A,
    )
)
connection_params_list.append(
    dict(
        pre=Multimeters.EXTENS_INTER_1A,
        post=NeuronGroups.EXTENS_INTER_1A,
    )
)
connection_params_list.append(
    dict(
        pre=Multimeters.FLEX_INTER_2,
        post=NeuronGroups.FLEX_INTER_2,
    )
)
connection_params_list.append(
    dict(
        pre=Multimeters.EXTENS_INTER_2,
        post=NeuronGroups.EXTENS_INTER_2,
    )
)
connection_params_list.append(
    dict(
        pre=Multimeters.FLEX_MOTOR,
        post=NeuronGroups.FLEX_MOTOR,
    )
)
connection_params_list.append(
    dict(
        pre=Multimeters.EXTENS_MOTOR,
        post=NeuronGroups.EXTENS_MOTOR,
    )
)
