from .data import *

class Inst_memory:
    def __init__(self, size: int) -> None:
        self._mem = [default_instruction for i in range(size)]
        
    def get(self, addr: int) -> Instruction:
        return self._mem[addr]
    
    def set(self, addr: int, data: Instruction) -> None:
        self._mem[addr] = data