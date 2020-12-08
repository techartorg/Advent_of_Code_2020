# -*- coding: utf-8 -*-

from pathlib import Path
import sys

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
            print( args[ -1 ] )
            sys.exit( 0 )
        
        _visited_program_lines.add( args[ 0 ] )

        return func( *args )
    
    return wrapper_op_counter


@op_counter
def acc( *args ):
    val = int( args[ 1 ][ 1: ] )
    accumulator = args[ -1 ]
    if args[ 1 ][ :1 ] == '+':
        accumulator += val
    else:
        accumulator -= val    
    
    return args[ 0 ] + 1, accumulator
    

@op_counter
def jmp( *args ):
    val = int( args[ 1 ][ 1: ] )
    if args[ 1 ][ :1 ] == '+':
        return args[ 0 ] + val, args[ -1 ]
    
    return args[ 0 ] - val, args[ -1 ]


@op_counter
def nop( *args ):
    return args[ 0 ] + 1, args[ -1 ]


if __name__ == '__main__':
    _ISA = { 'acc' : acc ,
             'jmp' : jmp, 
             'nop' : nop, }

    accumulator = 0

    ins = [ x.strip( ).split( ' ' ) for x in ( Path.cwd( ) / '8_input.txt' ).open( ).readlines( ) ]
    line_num = 0
    while line_num <= len( ins ) - 1:
        op = ins[ line_num ]
        line_num, accumulator = _ISA.get( op[ 0 ] )(  line_num, op[ -1 ], accumulator )
            