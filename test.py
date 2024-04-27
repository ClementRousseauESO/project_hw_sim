from src import decode_inst
from src import cpu

c = cpu.Cpu()
c.process(decode_inst.decode_inst("inc r1"))
print(c.get_state())
