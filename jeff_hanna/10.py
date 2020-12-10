# -*- coding: utf-8 -*-

from contextlib import suppress
from pathlib import Path

_TEST_DATA = ( 28,
               33,
               18,
               42,
               31,
               14,
               46,
               20,
               48,
               47,
               24,
               23,
               49,
               45,
               19,
               38,
               39,
               11,
               1,
               32,
               25,
               35,
               8,
               17,
               7,
               9,
               4,
               2,
               34,
               10,
               3, )

def _part_1( adaptors ):
    num_1_volt_diffs = 1 # Why???
    num_3_volt_diffs = 1 # For the final apdator -> device

    for i, joltage in enumerate( adaptors ):
        with suppress( IndexError ):
            diff = adaptors[ i + 1 ] - joltage
            if diff == 1:
                num_1_volt_diffs += 1
            elif diff == 3:
                num_3_volt_diffs += 1
            
    return num_1_volt_diffs * num_3_volt_diffs


if __name__ == '__main__':
    # adaptors = sorted( _TEST_DATA )
    adaptors = sorted( [ int( x ) for x in ( Path.cwd( ) / '10_input.txt' ).open( ).readlines( ) ] )
    
    # Part 1
    print( _part_1( adaptors ) ) # higher than 1827