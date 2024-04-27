from .data import *
from dataclasses import dataclass

@dataclass
class Cpu_State:
    PC: int
    Regs : dict [Registers, int]

class Cpu:
    def __init__(self) -> None:
        regs = {}
        for r in Registers:
            regs[r] = 0
        self._state = Cpu_State(PC=0, Regs=regs)
        
    def process (self, i : Instruction) -> int:
        if i.i_type == Inst_Type.inc:
            self._state.Regs[i.op_1] += 1
        self._state.PC += 1
        return self._state.PC
            
    def get_state (self) -> Cpu_State:
        return self._state