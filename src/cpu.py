from .data import *
from dataclasses import dataclass
from .memory import Memory

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
        
    def step(self, mem: Memory) -> int:
        i = mem.get(self._state.PC)
        pc_increment = True
        if i.i_type == Inst_Type.inc:
            self._state.Regs[i.op_1] += 1
        elif i.i_type == Inst_Type.brel:
            self._state.PC += i.op_1
            pc_increment = False
        elif i.i_type == Inst_Type.call:
            self._push(self._state.LR, mem)
            self._state.LR = self._state.PC + 1
            self._state.PC = i.op_1
            pc_increment = False
        elif i.i_type == Inst_Type.ret:
            self._state.PC = self._state.LR
            self._state.LR = self._pop(mem)
            pc_increment = False
        elif i.i_type == Inst_Type.ldi:
            self._state.Regs[i.op_1] = i.op_2
        elif i.i_type == Inst_Type.lds:
            self._state.Regs[i.op_1] = mem.get(i.op_2)
        elif i.i_type == Inst_Type.sts:
            mem.set(i.op_1, self._state.Regs[i.op_2])
        elif i.i_type == Inst_Type.push:
            self._push(i.op_1, mem)
        elif i.i_type == Inst_Type.pop:
            self._state.Regs[i.op_1] = self._pop(mem)
        if pc_increment:
            self._state.PC += 1
        return self._state.PC
            
    def get_state(self) -> Cpu_State:
        return self._state
    
    def _push(self, d: int, mem: Memory) -> None:
        mem.set(self._state.Regs[Registers.sp], d)
        self._state.Regs[Registers.sp] -= 1
    
    def _pop(self, mem: Memory) -> int:
        self._state.Regs[Registers.sp] += 1
        ret = mem.get(self._state.Regs[Registers.sp])
        return ret