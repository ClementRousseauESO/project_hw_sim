from .data import *
import sys

def decode_inst (line : str, labels : dict[str, int]) -> tuple[str | None, Instruction | None]:
    s = list(filter(None, line.split(' ')))
    inst = _decode_inst(s, labels)
    if inst:
        return (None, inst)
    elif s[0][-1] == ':':
        label = s[0][:-1]
        if len(s) > 1:
            inst = _decode_inst(s[1:], labels)
        else:
            inst = None
        if inst:
            return (label, inst)
        else:
            return (label, None)
        
def _decode_inst (s : list[str], labels : dict[str, int]) -> Instruction | None:
    if s[0] in Inst_Type.__members__:
        i_type = Inst_Type[s[0]]
        op_1 = None
        op_2 = None
        if ',' in s[1]:
            ops = s[1].split(',')
            if len(ops) == 2:
                op_1 = _decode_op(ops[0], labels)
                op_2 = _decode_op(ops[1], labels)
            else:
                #TODO: handle error
                sys.exit(-1)
        else:
            op_1 = _decode_op(s[1], labels)
        return Instruction(i_type=i_type, op_1=op_1, op_2=op_2)
    else:
        return None
                
def _decode_op (op: str, labels: dict[str, int]) -> Registers | int | str:
    if op in Registers.__members__:
        return Registers[op]
    elif op[0] == '$':
        if is_hex(op[1:]):
            return int(op[1:], 16)
        else:
            #TODO: handle error
            sys.exit(-1)
    elif op[0:2] == "0x":
        if is_hex(op[2:]):
            return int(op[2:], 16)
        else:
            #TODO: handle error
            sys.exit(-1)
    elif op.isnumeric() or (op[0] == '-' and op[1:].isnumeric()):
        return int(op)
    else:
        return op
        
def is_hex(s : str) -> bool:
    for c in s:
        if ((c < '0' or c > '9') and (c < 'A' or c > 'F')):
            return False
    return True