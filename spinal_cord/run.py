import nest

from spinal_cord import util
from spinal_cord.neuron_network import NeuronNetwork
from spinal_cord.params.afferents import afferent_params
from spinal_cord.params.connections import connection_params_list
from spinal_cord.params.devices import device_params
from spinal_cord.params.neuron_groups import neuron_group_params
from spinal_cord.params.ees import ees_params
from spinal_cord.display_results import display_results


nest.Install("research_team_models")
nest.Install("neuron_simulator_models")

entity_params = dict()
entity_params.update(afferent_params)
entity_params.update(neuron_group_params)
entity_params.update(device_params)
entity_params.update(ees_params)

util.clean_previous_results()
layer1 = NeuronNetwork(entity_params, connection_params_list)

nest.Simulate(150.)

display_results()