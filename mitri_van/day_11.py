'''
--- Day 11: Seating System ---

Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#). For example, the initial seat layout might look like this:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL

Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:

	If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
	If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
	Otherwise, the seat's state does not change.

Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes occupied:

#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##

After a second round, the seats with four or more occupied adjacent seats become empty again:

#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##

This process continues for three more rounds:

#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##

#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##

#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##

At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people stop moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?

Your puzzle answer was 2361.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats - they care about the first seat they can see in each of those eight directions!

Now, instead of considering just the eight immediately adjacent seats, consider the first seat in each of those eight directions. For example, the empty seat below would see eight occupied seats:

.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....

The leftmost empty seat below would only see one empty seat, but cannot see any of the occupied ones:

.............
.L.L.#.#.#.#.
.............

The empty seat below would see no occupied seats:

.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.

Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied seats for an occupied seat to become empty (rather than four or more from the previous rules). The other rules still apply: empty seats that see no occupied seats become occupied, seats matching no rule don't change, and floor never changes.

Given the same starting layout as above, these new rules cause the seating area to shift around as follows:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL

#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##

#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#

#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#

Again, at this point, people stop shifting around and the seating area reaches equilibrium. Once this occurs, you count 26 occupied seats.

Given the new visibility method and the rule change for occupied seats becoming empty, once equilibrium is reached, how many seats end up occupied?

Your puzzle answer was 2119.

Both parts of this puzzle are complete! They provide two gold stars: **

'''

from collections import deque

test_data_1 = [ 'L.LL.LL.LL',
					 'LLLLLLL.LL',
					 'L.L.L..L..',
					 'LLLL.LL.LL',
					 'L.LL.LL.LL',
					 'L.LLLLL.LL',
					 '..L.L.....',
					 'LLLLLLLLLL',
					 'L.LLLLLL.L',
					 'L.LLLLL.LL' ]

test_data_2 = [ '.......#.',
					 '...#.....',
					 '.#.......',
					 '.........',
					 '..#L....#',
					 '....#....',
					 '.........',
					 '#........',
					 '...#.....' ]


test_data_3 = [ '.............',
					 '.L.L.#.#.#.#.',
					 ',.............' ]

test_data_4 = [ '.##.##.',
					 '#.#.#.#',
					 '##...##',
					 '...L...',
					 '##...##',
					 '#.#.#.#',
					 '.##.##.' ]

def get_occupied_seat( idx, row ):

	# Out of range error
	if 0 > idx or idx >= len( row ):
		return None

	if row[ idx ] == '#':
		return True

	elif row[ idx ] == 'L':
		return False

	elif row[ idx ] == '.':
		return None


def raycast_for_seat( vector, row_num, rows, seat_num ):
	row_width = len( rows[ 0 ] )
	row_idx = row_num + vector[ 1 ]
	seat_idx = seat_num + vector[ 0 ]
	is_occupied = False

	if row_idx < 0 or row_idx > len( rows ) - 1:
		return 0

	while 0 <= seat_idx < row_width:
		if 0 > row_idx or row_idx >= len( rows ):
			return 0

		is_occupied = get_occupied_seat( seat_idx, rows[ row_idx ] )

		if is_occupied == True:
			return 1
		elif is_occupied == False:
			return 0

		seat_idx += vector[ 0 ]
		row_idx += vector[ 1 ]


def check_adjacent_seats( row_num, rows, seat_num ):
	start_seat = seat_num - 1
	end_seat = seat_num + 2

	start_row = row_num - 1
	end_row = row_num + 2

	is_occupied = False
	occupied_seats = 0

	for row_idx in range( start_row, end_row ):
		# Out of range error
		if 0 > row_idx or row_idx >= len( rows ):
			continue
		row = list( rows[ row_idx ] )

		for seat_idx in range( start_seat, end_seat ):
			if row_idx == row_num and seat_idx == seat_num:
				continue
			is_occupied = get_occupied_seat( seat_idx, row )

			if is_occupied:
				occupied_seats += 1

	return occupied_seats


def check_visible_seats( row_num, rows, seat_num ):
	occupied_seats = 0
	is_occupied = False

	search_vectors = [ ( -1, -1 ), ( 0, -1 ), ( 1, -1 ),
							 ( -1, 0 ), ( 1, 0 ),
							 ( -1, 1 ), ( 0, 1 ), ( 1, 1 ) ]

	for vector in search_vectors:
		is_occupied = raycast_for_seat( vector, row_num, rows, seat_num )

		if is_occupied:
			occupied_seats += 1

	return occupied_seats


def take_seats( data, adjacent = True ):
	new_data = [ ]

	for row_num, row in enumerate( data ):
		seats = list( row )
		new_seats = list( row )

		for seat_num, seat in enumerate( seats ):
			if seat == '.':
				pass

			else:
				occupied_seats = 0
				if adjacent:
					occupied_seats = check_adjacent_seats( row_num, data, seat_num )

					if occupied_seats == 0 and seat == 'L':
						new_seats[ seat_num ] = '#'
					elif occupied_seats >= 4 and seat == '#':
						new_seats[ seat_num ] = 'L'

				else:
					occupied_seats = check_visible_seats( row_num, data, seat_num )

					if occupied_seats == 0 and seat == 'L':
						new_seats[ seat_num ] = '#'
					elif occupied_seats >= 5 and seat == '#':
						new_seats[ seat_num ] = 'L'


			result = ''.join( [ str( seat ) for seat in new_seats ] )

		new_data.append( result )
	return new_data


def get_occupied_seats( data, adjacent = True ):
	result = data
	old_result = [ ]
	i = 1

	# print( 'Pass #0')
	# for x in result:
		# print( '\t{0}'.format( x ) )
	# print( '' )

	while result != old_result:
		old_result = result.copy( )
		result = take_seats( result, adjacent = adjacent )

		# if old_result != result:
			# print( 'Pass #{0}'.format( i ) )
			# for x in result:
				# print( '\t{0}'.format( x ) )
			# print( '' )
		# i += 1

	n = sum( [ x.count( '#' ) for x in result ] )
	print( 'Occupied seats: {0}'.format( n ) )



if __name__ == "__main__":
	input = r'D:\Projects\Python\Personal\Advent_of_Code\2020\day_11_input.txt'
	# input = r'D:\Dropbox\Projects\Python\Advent_of_Code\2020\day_11_input.txt'

	data = [ ]

	with open( input, 'r' ) as input_file:
		data = [ line.strip( ) for line in input_file.readlines( ) ]

	get_occupied_seats( data )
	get_occupied_seats( data, adjacent = False )