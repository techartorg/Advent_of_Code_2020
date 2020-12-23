'''
--- Day 23: Crab Cups ---

The small crab challenges you to a game! The crab is going to mix up some cups, and you have to predict where they'll end up.

The cups will be arranged in a circle and labeled clockwise (your puzzle input). For example, if your labeling were 32415, there would be five cups in the circle; going clockwise around the circle from the first cup, the cups would be labeled 3, 2, 4, 1, 5, and then back to 3 again.

Before the crab starts, it will designate the first cup in your list as the current cup. The crab is then going to do 100 moves.

Each move, the crab does the following actions:

	The crab picks up the three cups that are immediately clockwise of the current cup. They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle.
	The crab selects a destination cup: the cup with a label equal to the current cup's label minus one. If this would select one of the cups that was just picked up, the crab will keep subtracting one until it finds a cup that wasn't just picked up. If at any point in this process the value goes below the lowest value on any cup's label, it wraps around to the highest value on any cup's label instead.
	The crab places the cups it just picked up so that they are immediately clockwise of the destination cup. They keep the same order as when they were picked up.
	The crab selects a new current cup: the cup which is immediately clockwise of the current cup.

For example, suppose your cup labeling were 389125467. If the crab were to do merely 10 moves, the following changes would occur:

-- move 1 --
cups: (3) 8  9  1  2  5  4  6  7
pick up: 8, 9, 1
destination: 2

-- move 2 --
cups:  3 (2) 8  9  1  5  4  6  7
pick up: 8, 9, 1
destination: 7

-- move 3 --
cups:  3  2 (5) 4  6  7  8  9  1
pick up: 4, 6, 7
destination: 3

-- move 4 --
cups:  7  2  5 (8) 9  1  3  4  6
pick up: 9, 1, 3
destination: 7

-- move 5 --
cups:  3  2  5  8 (4) 6  7  9  1
pick up: 6, 7, 9
destination: 3

-- move 6 --
cups:  9  2  5  8  4 (1) 3  6  7
pick up: 3, 6, 7
destination: 9

-- move 7 --
cups:  7  2  5  8  4  1 (9) 3  6
pick up: 3, 6, 7
destination: 8

-- move 8 --
cups:  8  3  6  7  4  1  9 (2) 5
pick up: 5, 8, 3
destination: 1

-- move 9 --
cups:  7  4  1  5  8  3  9  2 (6)
pick up: 7, 4, 1
destination: 5

-- move 10 --
cups: (5) 7  4  1  8  3  9  2  6
pick up: 7, 4, 1
destination: 3

-- final --
cups:  5 (8) 3  7  4  1  9  2  6

In the above example, the cups' values are the labels as they appear moving clockwise around the circle; the current cup is marked with ( ).

After the crab is done, what order will the cups be in? Starting after the cup labeled 1, collect the other cups' labels clockwise into a single string with no extra characters; each number except 1 should appear exactly once. In the above example, after 10 moves, the cups clockwise from 1 are labeled 9, 2, 6, 5, and so on, producing 92658374. If the crab were to complete all 100 moves, the order after cup 1 would be 67384529.

Using your labeling, simulate 100 moves. What are the labels on the cups after cup 1?

Your puzzle answer was 72496583.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

Due to what you can only assume is a mistranslation (you're not exactly fluent in Crab), you are quite surprised when the crab starts arranging many cups in a circle on your raft - one million (1000000) in total.

Your labeling is still correct for the first few cups; after that, the remaining cups are just numbered in an increasing fashion starting from the number after the highest number in your list and proceeding one by one until one million is reached. (For example, if your labeling were 54321, the cups would be numbered 5, 4, 3, 2, 1, and then start counting up from 6 until one million is reached.) In this way, every number from one through one million is used exactly once.

After discovering where you made the mistake in translating Crab Numbers, you realize the small crab isn't going to do merely 100 moves; the crab is going to do ten million (10000000) moves!

The crab is going to hide your stars - one each - under the two cups that will end up immediately clockwise of cup 1. You can have them if you predict what the labels on those cups will be when the crab is finished.

In the above example (389125467), this would be 934001 and then 159792; multiplying these together produces 149245887792.

Determine which two cups will end up immediately clockwise of cup 1. What do you get if you multiply their labels together?

'''

from collections import deque

test_data_1 = 389125467


def virginia_reel( cups ):
	d_cups = deque( cups )
	d_cups.rotate( -3 )
	cups = list( d_cups )

	return cups


def pick_destination_cup( cups, current_cup, picked_up_cups ):
	destination_cup = -1

	for n in reversed( range( 0, current_cup ) ):
		if n not in picked_up_cups:
			if n in cups:
				destination_cup = n

				return destination_cup

	for cup in reversed( sorted( cups ) ):
		if cup not in picked_up_cups:
			destination_cup = cup
			break

	return destination_cup

def shuffle_cups( cups, n ):
	'''
	pick up 3 cups (clockwise)
	pick destination cup with label equal to current cup - 1
		Keep subtracting 1 until you find an untouched cup (this round)
			pick highest cup otherwise
	drop picked up cups clockwise of destination cup
	pick current cup + 1
	'''

	picked_up_cups = cups[ n + 1:n + 4 ]
	current_cup = cups[ n ]
	destination_cup = pick_destination_cup( cups, current_cup, picked_up_cups )

	for i in range( n + 1, n + 4 ):
		cups.pop( n + 1 )

	idx = cups.index( destination_cup )
	# while idx <= n:
		# idx += 1

	# Just drop the cups at the end if the destination is the last cup
	if idx == len( cups ):
		cups.extend( picked_up_cups )

	else:
		for dropped_cup in picked_up_cups:
			idx += 1
			cups.insert( idx, dropped_cup )

	return cups, picked_up_cups, destination_cup


def play_game( raw_data, moves ):
	cups = [ int( x ) for x in str( raw_data ) ]

	current_cup = cups[ 0 ]
	for i in range( 0, moves ):
		print( '-- move {} --'.format( i + 1 ) )
		print( 'cups: {}'.format( ", ".join( map( str, [ x for x in cups ] ) ) ) )

		cup_idx = cups.index( current_cup )
		cups, pick_up, dest = shuffle_cups( cups, cup_idx )

		# current_cup = cups.index( cup_idx )
		# print( '\t\t\tcurrent cup: {}'.format( cups[ cup_idx ] ) )
		print( 'pick up: {}'.format( ", ".join( map( str, [ x for x in pick_up ] ) ) ) )
		print( 'destination: {}\n'.format( dest ) )

		new_cup = cups.index( current_cup )

		while new_cup > 4:
			cups = virginia_reel( cups )
			new_cup = cups.index( current_cup )
		current_cup = cups[ new_cup + 1  ]

	print( '-- final --' )
	print( 'cups: {}'.format( ", ".join( map( str, [ x for x in cups ] ) ) ) )
	print( 'Current cup: {}'.format( current_cup ) )

	result = deque( cups )
	idx_1 = result.index( 1 )
	result.rotate( -idx_1 )
	result.popleft( )
	print( 'Result: {}'.format( "".join( map( str, [ x for x in result ] ) ) ) )



DEBUG = True
if __name__ == "__main__":
	raw_data = 315679824

	play_game( raw_data, 100 )


