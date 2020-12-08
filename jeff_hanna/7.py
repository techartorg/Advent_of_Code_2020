# -*- coding: utf-8 -*-

from pathlib import Path

_MY_LUGGAGE_TYPE = 'shiny gold bag'


def _fing_recursive_search( luggage_type ):
    bag_list = [ x for x in luggage_instructions if luggage_type in [ y[ -1 ] for y in luggage_instructions.get( x ) ] ]
    for bl in bag_list:
        bag_list.extend( _fing_recursive_search( bl ) )

    return bag_list


def _another_fing_recursive_search( luggage_type ):
    total_count = 1
    for num, new_bag in luggage_instructions.get( luggage_type ):
        total_count += _another_fing_recursive_search( new_bag ) * num

    return total_count
    

if __name__ == '__main__':
    luggage_instructions = { }
    for inst in [ x.strip( ).rstrip( '.' ).split( 'contain' ) for x in ( Path.cwd( ) / '7_input.txt' ).open( ).readlines( ) ]:
        luggage_instructions.update( { inst[ 0 ].strip( ).replace( 'bags', 'bag' ): [ x.strip( ) for x in inst[ -1 ].replace( 'bags', 'bag').split( ',' ) ] } )

    for k, v in luggage_instructions.items( ):
        new_v = [ ]
        for x in v:
            if x[ 0 ].isdigit( ):
                new_v.append( ( int( x[ :1 ] ), x[ 2: ] ) )
                
        luggage_instructions.update( { k: new_v } )

    # Part 1
    print( len( set( _fing_recursive_search( _MY_LUGGAGE_TYPE ) ) ) )

    # Part 2
    print( _another_fing_recursive_search( _MY_LUGGAGE_TYPE ) - 1 )