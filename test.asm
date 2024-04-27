init:
            ldi     sp,1999
            brel    start

start:
            inc     r1
            brel    jmp_1
jmp_2:      brel    jmp_3
jmp_1:      inc     r1
            brel    jmp_2
jmp_3:      inc     r1
            call    sub_routine_1
            inc     r1
            brel    end

sub_routine_1:
            inc     r1
            call    sub_routine_2
            ret

sub_routine_2:
            inc     r1
            ret

end: