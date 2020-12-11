# -*- coding: utf-8 -*-

from contextlib import suppress
from pathlib import Path

_MIN_JOLTAGE = 1
_MAX_JOLTAGE = 3

def _part_1( adaptors ):
    num_1_volt_diffs = 0
    num_3_volt_diffs = 0
    
    for i, joltage in enumerate( adaptors ):
        with suppress( IndexError ):
            diff = adaptors[ i + 1 ] - joltage
            if diff == _MIN_JOLTAGE:
                num_1_volt_diffs += 1
            elif diff == _MAX_JOLTAGE:
                num_3_volt_diffs += 1
            
    return num_1_volt_diffs * num_3_volt_diffs


def _part_2( adaptors ):
    tree_sums = [ 1 ] + [ 0 ] * ( len( adaptors ) - 1 ) # each element contains the joltage sum of a possible chain of adaptors.
    for i, joltage in enumerate( adaptors ):
        j = i + 1
        while j < len( adaptors ) and adaptors[ j ] - joltage <= _MAX_JOLTAGE:
            tree_sums[ j ] += tree_sums[ i ]
            j += 1
        
    return tree_sums[ -1 ]



if __name__ == '__main__':
    adaptors = sorted( [ int( x ) for x in ( Path.cwd( ) / '10_input.txt' ).open( ).readlines( ) ] )
    
    # Account for the wall socket and the device.
    adaptors.insert( 0, 0 )
    adaptors.append( adaptors[ -1 ] + _MAX_JOLTAGE )
    
    # Part 1
    print( _part_1( adaptors ) )
    print( _part_2( adaptors[ : -1 ] ) ) 