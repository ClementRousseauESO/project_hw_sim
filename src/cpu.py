from .data import *
from dataclasses import dataclass

@dataclass
class Cpu_State:
    PC: int
    LR: int
    Regs : dict [Registers, int]

class Cpu:
    def __init__(self) -> None:
        regs = {}
        for r in Registers:
            regs[r] = 0
        self._state = Cpu_State(PC=0, LR=0, Regs=regs)
        
    def process (self, i : Instruction) -> int:
        pc_increment = True
        if i.i_type == Inst_Type.inc:
            self._state.Regs[i.op_1] += 1
        elif i.i_type == Inst_Type.brel:
            self._state.PC += i.op_1
            pc_increment = False
        elif i.i_type == Inst_Type.call:
            self._state.LR = self._state.PC + 1
            self._state.PC = i.op_1
            pc_increment = False
        elif i.i_type == Inst_Type.ret:
            self._state.PC = self._state.LR
            pc_increment = False
        if pc_increment:
            self._state.PC += 1
        return self._state.PC
            
    def get_state (self) -> Cpu_State:
        return self._state