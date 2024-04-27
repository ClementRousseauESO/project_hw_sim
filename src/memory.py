from .data import *
from .inst_memory import Inst_memory
import sys

INST_MEM_OFFSET = 0
INST_MEM_SIZE = 1000

class Memory:
    def __init__(self) -> None:
        self._inst_memory = Inst_memory(size=INST_MEM_SIZE)
        
    def get(self, addr: int) -> Instruction:
        if addr >= INST_MEM_OFFSET and addr < INST_MEM_OFFSET + INST_MEM_SIZE:
            return self._inst_memory.get(addr=addr)
        else:
            #TODO: handle error
            sys.exit(-1)
    
    def set(self, addr: int, data: Instruction) -> None:
        if addr >= INST_MEM_OFFSET and addr < INST_MEM_OFFSET + INST_MEM_SIZE:
            self._inst_memory.set(addr=addr, data=data)
        else:
            #TODO: handle error
            sys.exit(-1)