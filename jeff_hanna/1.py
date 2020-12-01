# -*- coding: utf-8 -*-

from itertools import permutations
from math import prod
from pathlib import Path

_r = 2 # Use 2 for puzzle 1.1 and 3 for puzzle 1.2
with ( Path.cwd( ) / '1_input.txt' ).open( ) as f:
    for x in permutations( [ int( x.strip( ) ) for x in f.readlines( ) ], r = _r ):
        if sum( x ) == 2020:
            print( prod( x ) )
            break