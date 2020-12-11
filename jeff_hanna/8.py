# -*- coding: utf-8 -*-

from pathlib import Path

_TEST_DATA = ( 'nop +0\n',
               'acc +1\n',
               'jmp +4\n',
               'acc +3\n',
               'jmp -3\n',
               'acc -99\n',
               'acc +1\n',
               'jmp -4\n',
               'acc +6\n', )

_visited_program_lines = set( )

def op_counter( func ):
    def wrapper_op_counter( *args ):
        if args[ 0 ] in _visited_program_lines:
            return -1, args[ 0 ], args[ -1 ]
        
        _visited_program_lines.add( args[ 0 ] )
        return func( *args )
    
    return wrapper_op_counter


@op_counter
def acc( *args ):
    val = int( args[ 1 ][ 1: ] )
    accumulator = args[ -1 ]
    accumulator += int( args[ 1 ] )    
    return 0, args[ 0 ] + 1, accumulator
    

@op_counter
def jmp( *args ):
    return 0, args[ 0 ] + int( args[ 1 ] ), args[ -1 ]


@op_counter
def nop( *args ):
    return 0, args[ 0 ] + 1, args[ -1 ]


if __name__ == '__main__':
    _ISA = { 'acc' : acc ,
             'jmp' : jmp, 
             'nop' : nop, }

    ins = [ x.strip( ).split( ' ' ) for x in ( Path.cwd( ) / '8_input.txt' ).open( ).readlines( ) ]
    
    # Part 1
    accumulator = 0
    line_num = 0
    run = True
    while run:
        op = ins[ line_num ]
        ret_code, line_num, accumulator = _ISA.get( op[ 0 ] )( line_num, op[ -1 ], accumulator )
        if ret_code < 0:
            print( accumulator )
            run = False
