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
    move_boat = False
    
    if hdg == 'F':
        hdg = compass[ 0 ]
        move_boat = True
    
    if hdg in 'SW':
        dist = -dist
    
    return( hdg, dist, move_boat )


def _rotate_waypoint( boat_pos_e, boat_pos_n, wp_pos_e, wp_pos_n, hdg, degrees,  ):
    # Assuming we only turn to a cardinal direction
    r_dist_e = wp_pos_e - boat_pos_e
    r_dist_n = wp_pos_n - boat_pos_n

    _hdg_convos = { 'ES': ( r_dist_n, -r_dist_e ),
                    'EW': ( -r_dist_e, -r_dist_n ),
                    'EN': ( -r_dist_n, r_dist_e ),
                    'SW': ( r_dist_n, -r_dist_e ),
                    'SN': ( -r_dist_e, -r_dist_n ),
                    'WN': ( r_dist_n, -r_dist_e ),
                    'SE': ( -r_dist_n, r_dist_e ),
                    'WS': ( -r_dist_n, r_dist_e ),
                    'NE': ( r_dist_n, -r_dist_e ),
                    'NW': ( -r_dist_n, r_dist_e ) }

    _hdg_convos.update( { 'WE': _hdg_convos.get( 'EW' ),
                          'NS': _hdg_convos.get( 'SN' ) } )

    cur_hdg = compass[ 0 ]
    if hdg == 'R':
        degrees = -degrees

    compass.rotate( degrees // 90 )
    new_hdg = compass[ 0 ]
    
    convolution = _hdg_convos.get( ''.join( [ cur_hdg, new_hdg ] ) )
    return ( boat_pos_e + convolution[ 0 ], boat_pos_n + convolution[ -1 ] )


def _move_boat( boat_pos_e, boat_pos_n, wp_pos_e, wp_pos_n, dist ):
    # calculate realtive distance from boat to waypoint.
    r_dist_e = wp_pos_e - boat_pos_e
    r_dist_n = wp_pos_n - boat_pos_n
    for d in range( abs ( dist ) ):
        boat_pos_e += r_dist_e
        boat_pos_n += r_dist_n

    wp_pos_e = boat_pos_e + r_dist_e
    wp_pos_n = boat_pos_n + r_dist_n

    return ( boat_pos_e, boat_pos_n, wp_pos_e, wp_pos_n )


def _part_1( instrs ):
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
        hdg, dist, _mb = _decoder( i )
        if hdg in 'LR':
            _change_heading( hdg, dist )
            continue

        elif hdg in 'EW':
            E_dist += dist
        else:
            N_dist += dist

    return( abs( N_dist ) + abs( E_dist ) )


def _part_2( instrs ):
    '''
    Before you can give the destination to the captain, you realize that the actual 
    action meanings were printed on the back of the instructions the whole time.

    Almost all of the actions indicate how to move a waypoint which is relative to 
    the ship's position:

    Action N means to move the waypoint north by the given value.
    Action S means to move the waypoint south by the given value.
    Action E means to move the waypoint east by the given value.
    Action W means to move the waypoint west by the given value.
    Action L means to rotate the waypoint around the ship left (counter-clockwise) 
    the given number of degrees.
    Action R means to rotate the waypoint around the ship right (clockwise) the 
    given number of degrees.
    Action F means to move forward to the waypoint a number of times equal to the 
    given value.
    The waypoint starts 10 units east and 1 unit north relative to the ship. The 
    waypoint is relative to the ship; that is, if the ship moves, the waypoint moves 
    with it.
    '''
    
    boat_pos_e = 0
    boat_pos_n = 0
    wp_pos_e = boat_pos_e + 10
    wp_pos_n = boat_pos_n + 1

    for i in instrs:
        hdg, dist, move_boat = _decoder( i )
        
        if move_boat:
            boat_pos_e, boat_pos_n, wp_pos_e, wp_pos_n = _move_boat( boat_pos_e,
                                                                     boat_pos_n,
                                                                     wp_pos_e,
                                                                     wp_pos_n,
                                                                     dist )
            continue

        if hdg in 'LR':
            wp_pos_e, wp_pos_n = _rotate_waypoint( boat_pos_e,
                                                   boat_pos_n,
                                                   wp_pos_e,
                                                   wp_pos_n,
                                                   hdg, 
                                                   dist )
            continue

        elif hdg in 'EW':
            wp_pos_e += dist
        else:
            wp_pos_n += dist

    return( abs( boat_pos_e ) + abs( boat_pos_n ) )


    
if __name__ == '__main__':
    instrs = [ x.strip( ) for x in ( Path.cwd( ) / '12_input.txt' ).open( ).readlines( ) ]
    
    # Part 1
    print( _part_1( instrs ) )

    # Reset the compass
    compass = deque( [ 'E', 'S', 'W', 'N' ] )

    # Part 2
    print( _part_2( instrs ) )
    