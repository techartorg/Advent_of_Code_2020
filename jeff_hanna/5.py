# -*- coding: utf-8 -*-

from pathlib import Path

_ROWS = 128
_SEATS_PER_ROW = 8

def decode_seat_bsp( seat ):
    row_range = range( _ROWS )
    seat_range = range( _SEATS_PER_ROW )

    for x in seat:
        if x == 'F':
            row_range = row_range[ :len( row_range ) // 2 ]
        elif x == 'B':
            row_range = row_range[ len( row_range ) // 2: ]
        elif x == 'R':
            seat_range = seat_range[ len( seat_range ) // 2: ]
        else: # x == 'L':
            seat_range = seat_range[ :len( seat_range ) // 2 ]

    return ( row_range[ 0 ], seat_range[ 0 ] )


if __name__ == '__main__':
    decoded_seats = ( decode_seat_bsp( x.strip( ) ) for x in ( Path.cwd( ) / '5_input.txt' ).open( ) )
    seat_ids = sorted( ( row * 8 + seat for row, seat in decoded_seats ) )

    # Part 1
    print( seat_ids[ -1 ] )

    # Part 2
    my_seat_id = set( range( seat_ids[ 0 ], seat_ids[ -1 ] ) ).difference( seat_ids ).pop( )
    print( my_seat_id )
    