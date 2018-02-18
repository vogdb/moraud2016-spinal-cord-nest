### About

A NEST implementation of an existing [spinal cord model made in Neuron](https://senselab.med.yale.edu/ModelDB/showmodel.cshtml?model=189786) by Moraud EM, Capogrosso M.

#### Network Topology
<img src="/diagrams/network-topology.svg" alt="Network Topology" height=400/>

<table>
  <tr>
    <th colspan=2>Used Abbreviations</th>
  </tr>
  <tr>
    <th>Mn</th>
    <td>Motoneurons</td>
  </tr>
  <tr>
    <th>1A int</th>
    <td>Inhibitory Interneurons that are directly excited by 1A Afferents</td>
  </tr>
  <tr>
    <th>2 int</th>
    <td>Excitatory Interneurons that are directly excited by 2 Afferents</td>
  </tr>
  <tr>
    <th>1a</th>
    <td>Projections from 1A Afferents</td>
  </tr>
  <tr>
    <th>2</th>
    <td>Projections from 2 Afferents</td>
  </tr>
</table>

#### Network Implementation
The topology is good but the real implementation requires more additional neuron groups and generators. Below are all necessary additions.

<img src="/diagrams/network-implementation.svg" alt="Network Implementation" height=400/>

<table>
  <tr>
    <th colspan=2>Used Abbreviations</th>
  </tr>
  <tr>
    <th>EES</th>
    <td>Electrical Epidural stimulation</td>
  </tr>
  <tr>
    <th>1A nat</th>
    <td>Spike generators that simulate natural firing of 1A afferents</td>
  </tr>
  <tr>
    <th>2 nat</th>
    <td>Spike generators that simulate natural firing of 2 Afferents</td>
  </tr>
  <tr>
    <th>1A med</th>
    <td>Mediator neurons to summate together EES and natural firing of 1A Afferents</td>
  </tr>
  <tr>
    <th>2 med</th>
    <td>Mediator neurons to summate together EES and natural firing of 2 Afferents</td>
  </tr>
</table>

### Usage

This project was verified on *Python 3.5* and *NEST 2.14.0*. It also uses a custom NEST model [hh_moto_5ht](https://github.com/research-team/hh-moto-5ht).