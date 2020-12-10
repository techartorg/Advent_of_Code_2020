# -*- coding: utf-8 -*-

from contextlib import suppress
from pathlib import Path

def _part_1( adaptors ):
    num_1_volt_diffs = 0
    num_3_volt_diffs = 0
    
    for i, joltage in enumerate( adaptors ):
        with suppress( IndexError ):
            diff = adaptors[ i + 1 ] - joltage
            if diff == 1:
                num_1_volt_diffs += 1
            elif diff == 3:
                num_3_volt_diffs += 1
            
    return num_1_volt_diffs * num_3_volt_diffs


if __name__ == '__main__':
    adaptors = sorted( [ int( x ) for x in ( Path.cwd( ) / '10_input.txt' ).open( ).readlines( ) ] )
    
    # Account for the wall socket and the device.
    adaptors.insert( 0, 0 )
    adaptors.append( adaptors[ -1 ] + 3 )
    
    # Part 1
    print( _part_1( adaptors ) ) # higher than 1827