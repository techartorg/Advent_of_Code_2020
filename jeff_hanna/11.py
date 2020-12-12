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


def __empty_seat_check( i, seat, row, prev_row, next_row ):
    '''
    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    '''

    adjacent_count = 0
    # Current Row
    if i == 0 or i == len( row ) - 1: # left and right seats
        adjacent_count += 3 # horiz, diagonal prev, and diagonal next
    if i != 0 and row[ i - 1 ] != '#':
        adjacent_count += 1 
    if i != len( row ) - 1 and row[ i + 1 ] != '#':
        adjacent_count += 1

    # Prev and Next rows
    for j in range( i - 1, i + 2 ):
        #with suppress( IndexError ):
        if j >= 0 and j <= len( row ) - 1:
            if prev_row[ j ] != '#':
                adjacent_count += 1
            if next_row[ j ] != '#':
                adjacent_count += 1
    
    new_seat = '#' if adjacent_count == 8 else seat
    return new_seat


def __occupied_seat_check( i, seat, row, prev_row, next_row ):
    '''
    If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.
    '''
    
    adjacent_count = 0

    # Current Row
    if i != 0 and row[ i - 1 ] == '#':
        adjacent_count += 1
    if i != len( row ) - 1 and row[ i + 1 ] == '#':
        adjacent_count += 1

    # Prev and Next rows
    for j in range( i - 1, i + 2 ):
        if j >= 0 and j <= len( row ) - 1:
            if prev_row[ j ] == '#':
                adjacent_count += 1
            if next_row[ j ] == '#':
                adjacent_count += 1

    new_seat =  'L' if adjacent_count >= 4 else seat
    return new_seat


def _seat_check( row, prev_row, next_row ):
    new_row = ''
    for i, seat in enumerate( row ):        
                
        # Floor
        if seat == '.':
            new_row += '.'
            continue

        # Empty seat
        elif seat == 'L':
            new_row += __empty_seat_check( i, seat, row, prev_row, next_row )
          
        # Occupied Seat
        else: # seat == '#':
            new_row += __occupied_seat_check( i, seat, row, prev_row, next_row )
                        
    return new_row


def _part_1( seat_map ):
    iterations = 0
    
    run = True
    while run:
        new_seat_map = [ ]

        for i, row in enumerate( seat_map ):
            prev_row = seat_map[ i - 1 ] if i > 0 else ''.join( [ '.' ] * len( row ) )
            next_row = seat_map[ i + 1 ] if i < len( seat_map ) - 1 else ''.join( [ '.' ] * len( row ) )
            new_seat_map.append( _seat_check( row, prev_row, next_row ) )

        iterations += 1
        if new_seat_map == seat_map:
            run = False
            break
        
        seat_map = deepcopy( new_seat_map )

    return Counter( ''.join( seat_map ) ).get( '#' )





if __name__ == '__main__':
    seat_map = [ x.strip( ) for x in ( Path.cwd( ) / '11_input.txt' ).open( ).readlines( ) ]
    #seat_map = _TEST_DATA
    
    # Part 1
    print( _part_1( seat_map ) )