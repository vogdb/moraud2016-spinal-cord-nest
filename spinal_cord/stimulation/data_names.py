from enum import Enum


class NeuronTypes(Enum):
    ONE_A = 'Ia'
    TWO = 'II'
    MOTO = 'Mn'


class Muscles(Enum):
    FLEX = "TA"
    EXTENS = "GM"


class Interval(Enum):
    TWENTY = 20


class Speed(Enum):
    FIFTEEN = 15
    DEFAULT = ''
