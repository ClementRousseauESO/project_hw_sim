from src import decode_asm
from src import cpu
from src import memory

c = cpu.Cpu()
m = memory.Memory()
decode_asm.decode_asm('test.asm', c, m)
print(c.get_state())
