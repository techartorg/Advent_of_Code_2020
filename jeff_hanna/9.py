# -*- coding: utf-8 -*-

from collections import deque
from itertools import combinations
from pathlib import Path


def _find_num_without_prev_sum( nums, preamble_num ):
    d = deque( maxlen = 25 )
    for n in nums:
        if len( d ) != preamble_num:
            d.append( n )
            continue

        if not any( a + b == n for a, b, in combinations( d, 2 ) ):
            return n

        d.append( n )



def _find_sum_nums( nums, total ):
    for i in range( 2, len( nums ) ):
        d = deque( maxlen = i )
        for n in nums:
            d.append( n )
            if sum( d ) == total:
                return min( d ) + max( d )



if __name__ == '__main__':
    nums = [ int( x ) for x in ( Path.cwd( ) / '9_input.txt' ).open( ).readlines( ) ]
    
    # Part 1
    print( _find_num_without_prev_sum( nums, 25 ) )

    # Part 2
    print( _find_sum_nums( nums, _find_num_without_prev_sum( nums, 25 ) ) )
    