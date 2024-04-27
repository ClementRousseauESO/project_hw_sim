from .data import *
import sys

def decode_inst (line : str) -> str | Instruction:
    s = list(filter(None, line.split(' ')))
    if s[0] in Inst_Type.__members__:
        i_type = Inst_Type[s[0]]
        op_1 = None
        op_2 = None
        if ',' in s[1]:
            ops = s[1].split(',')
            if len(ops) == 2:
                op_1 = decode_op(ops[0])
                op_2 = decode_op(ops[1])
            else:
                #TODO: handle error
                sys.exit(-1)
        else:
            op_1 = decode_op(s[1])
        return Instruction(i_type=i_type, op_1=op_1, op_2=op_2)
                
def decode_op (op : str) -> Registers | int:
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
        #TODO: handle error
        sys.exit(-1)
        
def is_hex(s : str) -> bool:
    for c in s:
        if ((c < '0' or c > '9') and (c < 'A' or c > 'F')):
            return False
    return True