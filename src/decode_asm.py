from .decode_inst import decode_inst
from .data import *
from .cpu import *

def decode_asm (file: str, cpu: Cpu) -> None:
    with open(file) as f:
        lines = [line.rstrip() for line in f]
    d = decode_inst(lines[0])
    eof = False
    while not eof:
        if type(d) == Instruction:
            pc = cpu.process(d)
        if pc < len(lines):
            d = decode_inst(lines[pc])
        else:
            eof = True