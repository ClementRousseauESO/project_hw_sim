from dataclasses import dataclass
from enum import Enum

class Inst_Type(Enum):
    inc = 1
    brel = 2

class Registers(Enum):
    r1 = 1

@dataclass
class Instruction:
    i_type : Inst_Type
    op_1 : Registers | int | None
    op_2 : Registers | int | None