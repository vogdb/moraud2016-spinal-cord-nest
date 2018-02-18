### About

A NEST implementation of an existing [spinal cord model made in Neuron](https://senselab.med.yale.edu/ModelDB/showmodel.cshtml?model=189786) by Moraud EM, Capogrosso M.

#### Network Topology
<img src="/diagrams/network-topology.svg" alt="Network Topology" height=400/>

#### Network Implementation
The topology is good but the real implementation requires more additional neuron groups and generators. Below are all necessary additions.

<img src="/diagrams/network-implementation.svg" alt="Network Implementation" height=400/>

### Usage

This project was verified on *Python 3.5* and *NEST 2.14.0*. It also uses a custom NEST model [hh_moto_5ht](https://github.com/research-team/hh-moto-5ht).