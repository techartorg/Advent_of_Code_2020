# -*- coding: utf-8 -*-

from collections import deque, namedtuple
from contextlib import suppress
from copy import deepcopy
from math import prod
from pathlib import Path

def sledding( hill_data, slope ):
    tree_count = 0

    i = 0
    while i < len( hill_data ):
        [ x.rotate( slope.x ) for x in hill_data ]

        with suppress( IndexError ):
            if hill_data[ ( i := i + slope.y ) ][ 0 ] == '#': 
                tree_count += 1

    return tree_count


if __name__ == '__main__':
    Slope = namedtuple( 'Slope', [ 'x', 'y' ] )
    hill_data = [ deque( [ y for y in x ] ) for x in ( Path.cwd( ) / '3_input.txt' ).open( ).read( ).splitlines( ) ]

    slopes = ( Slope( x = -1, y = 1 ),
               Slope( x = -3, y = 1 ),
               Slope( x = -5, y = 1 ),
               Slope( x = -7, y = 1 ),
               Slope( x = -1, y = 2 ), )

    # Part 1
    print( sledding( deepcopy( hill_data ), slopes[ 1 ] ) )

    # Part 2
    trees = [ ]
    for s in slopes:
        trees.append( sledding( deepcopy( hill_data ), s ) )

    print( prod( trees ) )