from enum import Enum


class NetworkItemsNames(Enum):
    pass


class NeuronGroups(NetworkItemsNames):
    FLEX_MOTOR = "Flexor Motoneurons"
    EXTENS_MOTOR = "Extensor Motoneurons"
    FLEX_INTER_1A = "Flexor 1A Interneurons"
    EXTENS_INTER_1A = "Extensor 1A Interneurons"
    FLEX_INTER_2 = "Flexor 2 Interneurons"
    EXTENS_INTER_2 = "Extensor 2 Interneurons"
    # below are artificial neurons for modelling Afferents stimulation
    FLEX_AFFERENT_1A = "Flexor 1A artificial fibers"
    EXTENS_AFFERENT_1A = "Extensor 1A artificial fibers"
    FLEX_AFFERENT_2 = "Flexor 1A artificial fibers"
    EXTENS_AFFERENT_2 = "Extensor 1A artificial fibers"


class Afferents(NetworkItemsNames):
    FLEX_1A = "Flexor 1A fibers"
    EXTENS_1A = "Extensor 1a fibers"
    FLEX_2 = "Flexor 2 fibers"
    EXTENS_2 = "Extensor 2 fibers"


class Multimeters(NetworkItemsNames):
    FLEX_INTER_1A = "flex-inter1A-multimeter"
    EXTENS_INTER_1A = "extens-inter1A-multimeter"
    FLEX_INTER_2 = "flex-inter2-multimeter"
    EXTENS_INTER_2 = "extens-inter2-multimeter"
    FLEX_MOTOR = "flex-motor-multimeter"
    EXTENS_MOTOR = "extens-motor-multimeter"


class EES(NetworkItemsNames):
    EES = "EES"
