# -*- coding: utf-8 -*-

from collections import deque
from pathlib import Path

_TEST_DATA = ( 'F10',
               'N3',
               'F7',
               'R90',
               'F11' )

compass = deque( [ 'E', 'S', 'W', 'N' ] )

def _change_heading( hdg, degrees ):
    # Assuming we only turn to a cardinal direction
    if hdg == 'R':
        degrees = -degrees

    compass.rotate( degrees // 90 )
    return compass[ 0 ]


def _decoder( inst ):
    hdg = inst[ :1 ]
    dist = int( inst[ 1: ] )
    
    if hdg == 'F':
        hdg = compass[ 0 ]

    if hdg in 'SW':
        dist = -dist
    
    return( hdg, dist )


def _part1( instrs ):
    '''
    For example:

    F10
    N3
    F7
    R90
    F11
    These instructions would be handled as follows:

    F10 would move the ship 10 units east (because the ship starts by facing east) to east 10, north 0.
    N3 would move the ship 3 units north to east 10, north 3.
    F7 would move the ship another 7 units east (because the ship is still facing east) to east 17, north 3.
    R90 would cause the ship to turn right by 90 degrees and face south; it remains at east 17, north 3.
    F11 would move the ship 11 units south to east 17, south 8.
    At the end of these instructions, the ship's Manhattan distance (sum of the absolute values of its east/west position and its north/south position) from its starting position is 17 + 8 = 25.

    Figure out where the navigation instructions lead. What is the Manhattan distance between that location and the ship's starting position?
    '''

    N_dist = 0
    E_dist = 0
    for i in instrs:
        hdg, dist = _decoder( i )
        if hdg in 'LR':
            _change_heading( hdg, dist )
            continue

        elif hdg in 'NS':
            N_dist += dist
        else:
            E_dist += dist

    return( abs( N_dist ) + abs( E_dist ) )


if __name__ == '__main__':
    # instrs = _TEST_DATA
    instrs = ( x.strip( ) for x in ( Path.cwd( ) / '12_input.txt' ).open( ).readlines( ) )
    
    # Part 1
    print( _part1( instrs ) )
    