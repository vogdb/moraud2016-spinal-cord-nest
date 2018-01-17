from spinal_cord.network_items_names import NeuronGroups, Afferents, Multimeters

distr_normal_2 = {'distribution': 'normal', 'mu': 2.0, 'sigma': 0.175}  # 0.175^2 = 0.03
distr_normal_3 = {'distribution': 'normal', 'mu': 3.0, 'sigma': 0.175}  # 0.175^2 = 0.03
syn_default_model = 'static_synapse'

conn_all_to_all = {
    'rule': 'all_to_all'
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

######## FLEX SOURCES #########
# source is Afferents.FLEX_1A,

connection_params_list.append(
    dict(
        pre=Afferents.FLEX_1A,
        post=NeuronGroups.FLEX_MOTOR,
        syn_spec=syn_spec_afferent1a_motor,
        conn_spec=conn_spec_afferent1a_motor,
    )
)
connection_params_list.append(
    dict(
        pre=Afferents.FLEX_1A,
        post=NeuronGroups.FLEX_INTER_1A,
        syn_spec=syn_spec_afferent1a_inter1a,
        conn_spec=conn_spec_afferent1a_inter1a,
    )
)

# source is Afferents.FLEX_2
connection_params_list.append(
    dict(
        pre=Afferents.FLEX_2,
        post=NeuronGroups.FLEX_INTER_2,
        syn_spec=syn_spec_afferent2_inter2,
        conn_spec=conn_spec_afferent2_inter2,
    )
)
connection_params_list.append(
    dict(
        pre=Afferents.FLEX_2,
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
        post=NeuronGroups.EXTENS_MOTOR,
        syn_spec=syn_spec_afferent1a_motor,
        conn_spec=conn_spec_afferent1a_motor,
    )
)
connection_params_list.append(
    dict(
        pre=Afferents.EXTENS_1A,
        post=NeuronGroups.EXTENS_INTER_1A,
        syn_spec=syn_spec_afferent1a_inter1a,
        conn_spec=conn_spec_afferent1a_inter1a,
    )
)

# source is Afferents.EXTENS_2
connection_params_list.append(
    dict(
        pre=Afferents.EXTENS_2,
        post=NeuronGroups.EXTENS_INTER_2,
        syn_spec=syn_spec_afferent2_inter2,
        conn_spec=conn_spec_afferent2_inter2,
    )
)
connection_params_list.append(
    dict(
        pre=Afferents.EXTENS_2,
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
