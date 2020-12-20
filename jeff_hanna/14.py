# -*- coding: utf-8 -*-

from pathlib import Path

_PART_1_TEST_DATA = ( 'mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X\n',
                      'mem[8] = 11\n',
                      'mem[7] = 101\n',
                      'mem[8] = 0\n', )

_PART_2_TEST_DATA = ( 'mask = 000000000000000000000000000000X1001X\n',
                      'mem[42] = 100\n',
                      'mask = 00000000000000000000000000000000X0XX\n',
                      'mem[26] = 1\n' )


def _part_1( instructions ):
    '''
    After a brief inspection, you discover that the sea port's computer system 
    uses a strange bitmask system in its initialization program. Although you 
    don't have the correct decoder chip handy, you can emulate it in software!

    The initialization program (your puzzle input) can either update the bitmask 
    or write a value to memory. Values and memory addresses are both 36-bit 
    unsigned integers. For example, ignoring bitmasks for a moment, a line like 
    mem[8] = 11 would write the value 11 to memory address 8.

    The bitmask is always given as a string of 36 bits, written with the most 
    significant bit (representing 2^35) on the left and the least significant 
    bit (2^0, that is, the 1s bit) on the right. The current bitmask is applied 
    to values immediately before they are written to memory: a 0 or 1 overwrites 
    the corresponding bit in the value, while an X leaves the bit in the value 
    unchanged.

    Execute the initialization program. What is the sum of all values left in 
    memory after it completes? (Do not truncate the sum to 36 bits.)
    '''

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


def _part_2( instructions ):
    '''
    For some reason, the sea port's computer system still can't communicate with 
    your ferry's docking program. It must be using version 2 of the decoder chip!

    A version 2 decoder chip doesn't modify the values being written at all. 
    Instead, it acts as a memory address decoder. Immediately before a value is 
    written to memory, each bit in the bitmask modifies the corresponding bit of 
    the destination memory address in the following way:

    If the bitmask bit is 0, the corresponding memory address bit is unchanged.
    If the bitmask bit is 1, the corresponding memory address bit is overwritten 
    with 1.
    If the bitmask bit is X, the corresponding memory address bit is floating.
    A floating bit is not connected to anything and instead fluctuates 
    unpredictably. In practice, this means the floating bits will take on all 
    possible values, potentially causing many memory addresses to be written 
    all at once!

    Execute the initialization program using an emulator for a version 2 decoder 
    chip. What is the sum of all values left in memory after it completes?
    '''

    return -1


if __name__ == '__main__':
    # instructions = [ x.strip( ) for x in _PART_1_TEST_DATA ]
    # instructions = [ x.strip( ) for x in _PART_2_TEST_DATA ]
    instructions = [ x.strip( ) for x in ( Path.cwd( ) / '14_input.txt' ).open( ).readlines( ) ]

    # Part 1
    print( _part_1( instructions ) )

    # Part 2
    print( _part_2( instructions ) )
