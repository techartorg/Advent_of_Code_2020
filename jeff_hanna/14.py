# -*- coding: utf-8 -*-

from pathlib import Path

_TEST_DATA = ( 'mem[8] = 11\n',
               'mem[7] = 101\n',
               'mem[8] = 0\n', )


def _part_1( instructions ):
    mem = { }
    set_bits = 0
    clear_bits = 0

    for inst in instructions:
        ( ins, bits ) = inst.split( '=' )

        if ins.startswith( 'mask' ):
            set_bits = 0
            clear_bits = 0
            for bit in list( bits ) :                
                set_bits = set_bits << 1
                clear_bits = clear_bits << 1
                if bit.lower( ) == 'x':
                    continue

                if bit == '1':
                    set_bits |= 1
                elif bit == '0':
                    clear_bits |= 1
        else:
            val = int( bits.lstrip( ) )
            val|= set_bits
            val &= ~ clear_bits

            mem.update( { int( ins.split( '[' )[ -1 ].rstrip( ' ]' ) ): val } )

    return sum( mem.values( ) )


if __name__ == '__main__':
    # instructions = [ x.strip( ) for x in _TEST_DATA ]
    instructions = [ x.strip( ) for x in ( Path.cwd( ) / '14_input.txt' ).open( ).readlines( ) ]

    # Part 1
    print( _part_1( instructions ) )