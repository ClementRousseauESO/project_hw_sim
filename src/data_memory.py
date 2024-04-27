from .data import *

class Data_memory:
    def __init__(self, size: int) -> None:
        self._mem = [0 for i in range(size)]
        
    def get(self, addr: int) -> int:
        return self._mem[addr]
    
    def set(self, addr: int, data: int) -> None:
        self._mem[addr] = data