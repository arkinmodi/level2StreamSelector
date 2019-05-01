## @file StdntAllocTypes.py
#  @author Arkin Modi modia1
#  @brief Student Allocation Types Module
#  @date 11/02/2019

from SeqADT import *
from enum import Enum
from typing import NamedTuple


## @brief A data type that represents the genders
class GenT(Enum):
    male = 1
    female = 2


## @brief A data type that represents the departments
class DeptT(Enum):
    civil = 1
    chemical = 2
    electrical = 3
    mechanical = 4
    software = 5
    materials = 6
    engphys = 7


## @brief A data type that represents a student
class SInfoT(NamedTuple):
    fname: str
    lname: str
    gender: GenT
    gpa: float
    choices: SeqADT
    freechoice: bool
