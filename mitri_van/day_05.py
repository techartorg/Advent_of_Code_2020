'''
--- Day 5: Binary Boarding ---

You board your plane only to discover a new problem: you dropped your boarding pass! You aren't sure which seat is yours, and all of the flight attendants are busy with the flood of people that suddenly made it through passport control.

You write a quick program to use your phone's camera to scan all of the nearby boarding passes (your puzzle input); perhaps you can find your seat through process of elimination.

Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".

The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.

For example, consider just the first seven characters of FBFBBFFRLR:

	Start by considering the whole range, rows 0 through 127.
	F means to take the lower half, keeping rows 0 through 63.
	B means to take the upper half, keeping rows 32 through 63.
	F means to take the lower half, keeping rows 32 through 47.
	B means to take the upper half, keeping rows 40 through 47.
	B keeps rows 44 through 47.
	F keeps rows 44 through 45.
	The final F keeps the lower of the two, row 44.

The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.

For example, consider just the last 3 characters of FBFBBFFRLR:

	Start by considering the whole range, columns 0 through 7.
	R means to take the upper half, keeping columns 4 through 7.
	L means to take the lower half, keeping columns 4 through 5.
	The final R keeps the upper of the two, column 5.

So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.

Here are some other boarding passes:

	BFFFBBFRRR: row 70, column 7, seat ID 567.
	FFFBBBFRRR: row 14, column 7, seat ID 119.
	BBFFBBFRLL: row 102, column 4, seat ID 820.

As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?

Your puzzle answer was 908.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?

Your puzzle answer was 619.

Both parts of this puzzle are complete! They provide two gold stars: **

'''

import bisect

test_data_1 = [ 'FBFBBFFRLR' ]
test_data_2 = [ 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL' ]


def build_seats( rows, seats ):
	row_array = [ ]
	seat_array = [ ]

	row_array.extend( range( 0, rows ) )
	seat_array.extend( range( 0, seats ) )

	return row_array, seat_array


def validate_boarding_pass( boarding_pass ):
	row = boarding_pass[ :7 ]
	seat = boarding_pass[ 7: ]

	for idx, val in enumerate( row ):
		if val not in 'FB':
			return False

	for idx, val in enumerate( seat ):
		if val not in 'LR':
			return False

	return True, row, seat


def lookup_seat( lookup_val, boarding_pass, seating_section, debug = False ):
	idx_high = len( seating_section )
	idx_low = 0
	idx_mid = 0

	for step in boarding_pass:
		if step  == lookup_val[ 0 ]:
			idx_mid = bisect.bisect_left( seating_section, seating_section[ int( ( idx_high + idx_low ) / 2 ) ], lo = idx_low, hi = idx_high )
			idx_high = idx_mid
			if debug:
				print( '[ {0} ] {1} : {2} : {3}'.format( step, idx_low, idx_mid, idx_high ) )
		elif step == lookup_val[ 1 ]:
			idx_mid = bisect.bisect_left(  seating_section, seating_section[ int( ( idx_high + idx_low ) / 2 ) ], lo = idx_low, hi = idx_high )
			idx_low = idx_mid
			if debug:
				print( '[ {0} ] {1} : {2} : {3}'.format( step, idx_low, idx_mid, idx_high ) )

	return idx_low


def find_seat( boarding_pass, rows, seats ):
	row_num = 0
	seat_num = 0
	result, row_pass, seat_pass = validate_boarding_pass( boarding_pass )

	row_num = lookup_seat( 'FB', row_pass, rows )
	seat_num = lookup_seat( 'LR', seat_pass, seats )#, debug = True )

	seat = row_num * 8 + seat_num

	return seat


def find_my_seat( assigned_seats ):
	total_seats = [ ]
	total_seats.extend( range( 0, len( assigned_seats ) ) )

	lowest_seat_num = sorted( assigned_seats )[ 0 ]
	my_seat = [ seat for seat in total_seats[ lowest_seat_num: ] if seat not in assigned_seats ][ 0 ]

	return my_seat



if __name__ == "__main__":
	input = r'D:\Projects\Python\Personal\Advent_of_Code\2020\day_05_input.txt'
	# input = r'D:\Dropbox\Projects\Python\Advent_of_Code\2020\day_05_input.txt'

	data = [ ]
	row = [ ]
	seat = [ ]

	valid_passes = [ ]
	invalid_passes = [ ]
	assigned_seats = [ ]

	with open( input, 'r' ) as input_file:
		data = [ line.strip( ) for line in input_file.readlines( ) ]

	for boarding_pass in data:
		result = validate_boarding_pass( boarding_pass )
		row, seat = build_seats( 128, 8 )
		assigned_seat = find_seat( boarding_pass, row, seat )

		if result:
			valid_passes.append( boarding_pass )
		else:
			invalid_passes.append( boarding_pass )

		assigned_seats.append( assigned_seat )

	my_seat = find_my_seat( assigned_seats )

	print( 'Highest assigned seat number: {0}'.format( sorted( assigned_seats )[ -1 ] ) )
	print( 'My seat number: {0}'.format( my_seat ) )
	print( "\nValid number of entries: {0}\t\t\nInvalid number of entries: {1}".format( len( valid_passes), len( invalid_passes ) ) )

