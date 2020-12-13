# -*- coding: utf-8 -*-

from collections import Counter
from copy import deepcopy
from pathlib import Path

_TEST_DATA = ( 'L.LL.LL.LL',
               'LLLLLLL.LL',
               'L.L.L..L..',
               'LLLL.LL.LL',
               'L.LL.LL.LL',
               'L.LLLLL.LL',
               '..L.L.....',
               'LLLLLLLLLL',
               'L.LLLLLL.L',
               'L.LLLLL.LL' )


def __empty_seat_cast( seat_idx, seat, row_idx, row, seat_map ):
    '''
    Need to account for left, top, right, and bottom borders and cast rays
    out in the 8 cardinal directions until a seat is hit.
    The same empty seat rules as in __empty_seat_check( ) apply
    '''

    adjacent_count = 0

    # N
    for r in range( row_idx - 1, -1, -1 ):
        check_seat = seat_map[ r ][ seat_idx ]
        if check_seat == '.':
            continue
        elif check_seat != '#':
            adjacent_count += 1
            break
    
    else:
        adjacent_count += 1
    
    # NE
    s_cnt = 0
    found = False
    for r in range( row_idx - 1, -1, -1 ):
        s = seat_idx + s_cnt + ( row_idx - ( row_idx - 1 ) )       
        if s < len( row ):
            check_seat = seat_map[ r ][ s ]
            if check_seat == '.':
                s_cnt += 1
                continue
            elif check_seat != '#':
                adjacent_count += 1
                break
            else:
                found = True
    else:
        if not found:
            adjacent_count += 1
    
    # E
    found = False
    for s in range( seat_idx + 1, len( row ) ):
        check_seat = seat_map[ row_idx ][ s ]
        if check_seat == '.':
            continue
        elif check_seat != '#':
            adjacent_count += 1
            break
        else:
            found = True
    else:
        if not found:
            adjacent_count += 1
   
    # SE
    s_cnt = 0
    found = False
    for r in range( row_idx + 1, len( seat_map ) ):
        s = seat_idx + s_cnt + ( ( row_idx + 1 ) - row_idx )
        if s < len( row ):
            check_seat = seat_map[ r ][ s ]
            if check_seat == '.':
                s_cnt += 1
                continue
            elif check_seat != '#':
                adjacent_count += 1
                break
            else:
                found = True
    else:
        if not found:
            adjacent_count += 1

    # S
    found = False
    for r in range( row_idx + 1, len( seat_map ) ):
        check_seat = seat_map[ r ][ seat_idx ]
        if check_seat == '.':
            continue
        elif check_seat != '#':
            adjacent_count += 1
            break
        else:
            found = True
    else:
        if not found:
            adjacent_count += 1

    # SW
    found = False
    s_cnt = 0
    for r in range( row_idx + 1, len( seat_map ) ):
        s = seat_idx - s_cnt - ( ( row_idx + 1 ) - row_idx )
        if s >= 0:
            check_seat = seat_map[ r ][ s ]
            if check_seat == '.':
                s_cnt += 1
                continue
            elif check_seat != '#':
                adjacent_count += 1
                break
            else:
                found = True
    else:
        if not found:
            adjacent_count += 1

    # W
    found = False
    for s in range( seat_idx - 1, -1, -1 ):
        check_seat = seat_map[ row_idx ][ s ]
        if check_seat == '.':
            continue
        elif check_seat != '#':
            adjacent_count += 1
            break
        else:
            found = True
    else:
        if not found:
            adjacent_count += 1

    # NW
    found = False
    s_cnt = 0
    for r in range( row_idx - 1, -1, -1 ):
        s = seat_idx - s_cnt - ( row_idx - ( row_idx - 1 ) )
        if s >= 0:
            check_seat = seat_map[ r ][ s ]
            if check_seat == '.':
                s_cnt += 1
                continue
            elif check_seat != '#':
                adjacent_count += 1
                break
            else:
                found = True
    else:
        if not found:
            adjacent_count += 1

    new_seat = '#' if adjacent_count == 8 else seat
    return new_seat


def __empty_seat_check( seat_idx, seat, row_idx, row, seat_map ):
    '''
    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    '''

    prev_row = seat_map[ row_idx - 1 ] if row_idx > 0 else ''.join( [ '.' ] * len( row ) )
    next_row = seat_map[ row_idx + 1 ] if row_idx < len( seat_map ) - 1 else ''.join( [ '.' ] * len( row ) )
    adjacent_count = 0

    # Current Row
    if seat_idx == 0 or seat_idx == len( row ) - 1: # left and right seats
        adjacent_count += 3 # horiz, diagonal prev, and diagonal next
    if seat_idx != 0 and row[ seat_idx - 1 ] != '#':
        adjacent_count += 1 
    if seat_idx != len( row ) - 1 and row[ seat_idx + 1 ] != '#':
        adjacent_count += 1

    # Prev and Next rows
    for j in range( seat_idx - 1, seat_idx + 2 ):
        #with suppress( IndexError ):
        if j >= 0 and j <= len( row ) - 1:
            if prev_row[ j ] != '#':
                adjacent_count += 1
            if next_row[ j ] != '#':
                adjacent_count += 1
    
    new_seat = '#' if adjacent_count == 8 else seat
    return new_seat


def __occupied_seat_cast( seat_idx, seat, row_idx, row, seat_map ):
    '''
    Need to account for left, top, right, and bottom borders and cast rays
    out in the 8 cardinal directions until a seat is hit.
    The same occupied seat rules as in __occupied_seat_check( ) apply. But now 
    There must be 5 or more visible occupied seats for the seat being checked to emtpy.
    '''

    adjacent_count = 0
    
    # N
    for r in range( row_idx - 1, -1, -1 ):
        check_seat = seat_map[ r ][ seat_idx ]
        if check_seat == '.':
            continue
        elif check_seat == '#':
            adjacent_count += 1
            break

    # NE
    s_cnt = 0
    for r in range( row_idx - 1, -1, -1 ):
        s = seat_idx + s_cnt + ( row_idx - ( row_idx - 1 ) )       
        if s < len( row ):
            check_seat = seat_map[ r ][ s ]
            if check_seat == '.':
                s_cnt += 1
                continue
            elif check_seat == '#':
                adjacent_count += 1
                break
    
    # E
    for s in range( seat_idx + 1, len( row ) ):
        check_seat = seat_map[ row_idx ][ s ]
        if check_seat == '.':
            continue
        elif check_seat == '#':
            adjacent_count += 1
            break

    # SE
    s_cnt = 0
    for r in range( row_idx + 1, len( seat_map ) ):
        s = seat_idx + s_cnt + ( ( row_idx + 1 ) - row_idx )
        if s < len( row ):
            check_seat = seat_map[ r ][ s ]
            if check_seat == '.':
                s_cnt += 1
                continue
            elif check_seat == '#':
                adjacent_count += 1
                break

    # S
    for r in range( row_idx + 1, len( seat_map ) ):
        check_seat = seat_map[ r ][ seat_idx ]
        if check_seat == '.':
            continue
        elif check_seat == '#':
            adjacent_count += 1
            break
    
    # SW
    s_cnt = 0
    for r in range( row_idx + 1, len( seat_map ) ):
        s = seat_idx - s_cnt - ( ( row_idx + 1 ) - row_idx )
        if s >= 0:
            check_seat = seat_map[ r ][ s ]
            if check_seat == '.':
                s_cnt += 1
                continue
            elif check_seat == '#':
                adjacent_count += 1
                break
    
    # W
    for s in range( seat_idx - 1, -1, -1 ):
        check_seat = seat_map[ row_idx ][ s ]
        if check_seat == '.':
            continue
        elif check_seat == '#':
            adjacent_count += 1
            break
    
    # NW
    s_cnt = 0
    for r in range( row_idx - 1, -1, -1 ):
        s = seat_idx - s_cnt - ( row_idx - ( row_idx - 1 ) )
        if s >= 0:
            check_seat = seat_map[ r ][ s ]
            if check_seat == '.':
                s_cnt += 1
                continue
            elif check_seat == '#':
                adjacent_count += 1
                break
   
    new_seat = 'L' if adjacent_count >= 5 else seat
    return new_seat


def __occupied_seat_check( seat_idx, seat, row_idx, row, seat_map ):
    '''
    If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.
    '''
    
    prev_row = seat_map[ row_idx - 1 ] if row_idx > 0 else ''.join( [ '.' ] * len( row ) )
    next_row = seat_map[ row_idx + 1 ] if row_idx < len( seat_map ) - 1 else ''.join( [ '.' ] * len( row ) )
    adjacent_count = 0

    # Current Row
    if seat_idx != 0 and row[ seat_idx - 1 ] == '#':
        adjacent_count += 1
    if seat_idx != len( row ) - 1 and row[ seat_idx + 1 ] == '#':
        adjacent_count += 1

    # Prev and Next rows
    for j in range( seat_idx - 1, seat_idx + 2 ):
        if j >= 0 and j <= len( row ) - 1:
            if prev_row[ j ] == '#':
                adjacent_count += 1
            if next_row[ j ] == '#':
                adjacent_count += 1

    new_seat =  'L' if adjacent_count >= 4 else seat
    return new_seat


def _seat_check( row_idx, row, seat_map, part ):
    new_row = ''
    for seat_idx, seat in enumerate( row ):        
        # Floor
        if seat == '.':
            new_row += '.'
            continue        

        # Empty seat
        elif seat == 'L':
            func = __empty_seat_check if part == 'part1' else __empty_seat_cast
            new_row += func( seat_idx, seat, row_idx, row, seat_map )
          
        # Occupied Seat
        else: # seat == '#':
            func = __occupied_seat_check if part == 'part1' else __occupied_seat_cast
            new_row += func( seat_idx, seat, row_idx, row, seat_map )

    return new_row


def _main( seat_map, part ):
    iterations = 0
    
    run = True
    while run:
        new_seat_map = [ ]

        for row_idx, row in enumerate( seat_map ):
            new_seat_map.append( _seat_check( row_idx, row, seat_map, part ) )

        iterations += 1
        if new_seat_map == seat_map:
            run = False
            break
        
        seat_map = deepcopy( new_seat_map )

    return Counter( ''.join( seat_map ) ).get( '#' )





if __name__ == '__main__':
    # seat_map = [ x.strip( ) for x in ( Path.cwd( ) / '11_input.txt' ).open( ).readlines( ) ]
    seat_map = _TEST_DATA
    
    # Part 1
    # print( _main( seat_map, 'part1' ) )

    # Part 2
    print( _main( seat_map, 'part2' ) )