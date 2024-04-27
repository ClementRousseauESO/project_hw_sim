from .data import *
from .inst_memory import Inst_memory
from .data_memory import Data_memory
import sys

INST_MEM_START = 0
INST_MEM_SIZE = 1000
INST_MEM_END = INST_MEM_START + INST_MEM_SIZE
DATA_MEM_START = 1000
DATA_MEM_SIZE = 1000
DATA_MEM_END = DATA_MEM_START + DATA_MEM_SIZE

class Memory:
    def __init__(self) -> None:
        self._inst_memory = Inst_memory(size=INST_MEM_SIZE)
        self._data_memory = Data_memory(size=DATA_MEM_SIZE)
        
    def get(self, addr: int) -> Instruction | int:
        if addr >= INST_MEM_START and addr < INST_MEM_END:
            return self._inst_memory.get(addr=addr-INST_MEM_START)
        if addr >= DATA_MEM_START and addr < DATA_MEM_END:
            return self._data_memory.get(addr=addr-DATA_MEM_START)
        else:
            #TODO: handle error
            sys.exit(-1)
    
    def set(self, addr: int, data: Instruction | int) -> None:
        if addr >= INST_MEM_START and addr < INST_MEM_END and type(data) == Instruction:
            self._inst_memory.set(addr=addr-INST_MEM_START, data=data)
        elif addr >= DATA_MEM_START and addr < DATA_MEM_END and type(data) == int:
            self._data_memory.set(addr=addr-DATA_MEM_START, data=data)
        else:
            #TODO: handle error
            sys.exit(-1)