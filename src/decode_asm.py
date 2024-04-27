from .decode_inst import decode_inst
from .data import *
from .cpu import *
from .memory import *

def decode_asm (file: str, cpu: Cpu, mem : Memory) -> None:
    pc = 0
    last_inst = _fill_inst_mem(file=file, mem=mem)
    while pc < last_inst:
        pc = cpu.step(mem)
            
def _fill_inst_mem(file: str, mem: Memory) -> int:
    labels = {}
    cur_inst_addr = 0
    max_addr = 0
    instructions: dict[int, Instruction] = {}
    with open(file) as f:
        for line in f:
            l = line.rstrip()
            label, inst = decode_inst(line=l, labels=labels)
            if label:
                labels[label] = cur_inst_addr
            if inst:
                instructions[cur_inst_addr] = inst
                cur_inst_addr += 1
                if cur_inst_addr > max_addr:
                    max_addr = cur_inst_addr
    for addr, i in instructions.items():
        if type(i.op_1) == str:
            i.op_1 = _replace_label(i_type=i.i_type, op=i.op_1, addr=addr, labels=labels)
        if type(i.op_2) == str:
            i.op_2 = _replace_label(i_type=i.i_type, op=i.op_2, addr=addr, labels=labels)
        mem.set(addr=addr, data=i)
    return max_addr

def _replace_label(i_type: Inst_Type, op: str, addr: int, labels: dict[str, int]) -> Registers | int:
    if op in labels:
        d = labels[op]
        if i_type == Inst_Type.inc or i_type == Inst_Type.push or i_type == Inst_Type.pop:
            if type(d) == str and d in Registers.__members__:
                return Registers[d]
            else:
                #TODO: Handle error
                sys.exit(-1)
        elif i_type == Inst_Type.brel:
            if type(d) == int:
                return d - addr
            else:
                #TODO: Handle error
                sys.exit(-1)
        elif i_type == Inst_Type.call:
            if type(d) == int:
                return d
            else:
                #TODO: Handle error
                sys.exit(-1)
        elif i_type == Inst_Type.ldi or i_type == Inst_Type.lds or i_type == Inst_Type.sts:
            if type(d) == str and d in Registers.__members__:
                return Registers[d]
            elif type(d) == int:
                return d
            else:
                #TODO: Handle error
                sys.exit(-1)
    else:
        #TODO: Handle error
        sys.exit(-1)