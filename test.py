from src import decode_asm
from src import cpu

c = cpu.Cpu()
decode_asm.decode_asm('test.asm', c)
print(c.get_state())
