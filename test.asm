start:
            inc     r1
            brel    jmp_1
jmp_2:      brel    jmp_3
jmp_1:      inc     r1
            brel    jmp_2
jmp_3:      inc     r1
            call    sub_routine
            inc     r1
            brel    end

sub_routine:
            inc     r1
            ret

end: