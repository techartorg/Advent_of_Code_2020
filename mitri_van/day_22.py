'''
--- Day 22: Crab Combat ---

It only takes a few hours of sailing the ocean on a raft for boredom to sink in. Fortunately, you brought a small deck of space cards! You'd like to play a game of Combat, and there's even an opponent available: a small crab that climbed aboard your raft before you left.

Fortunately, it doesn't take long to teach the crab the rules.

Before the game starts, split the cards so each player has their own deck (your puzzle input). Then, the game consists of a series of rounds: both players draw their top card, and the player with the higher-valued card wins the round. The winner keeps both cards, placing them on the bottom of their own deck so that the winner's card is above the other card. If this causes a player to have all of the cards, they win, and the game ends.

For example, consider the following starting decks:

Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10

This arrangement means that player 1's deck contains 5 cards, with 9 on top and 1 on the bottom; player 2's deck also contains 5 cards, with 5 on top and 10 on the bottom.

The first round begins with both players drawing the top card of their decks: 9 and 5. Player 1 has the higher card, so both cards move to the bottom of player 1's deck such that 9 is above 5. In total, it takes 29 rounds before a player has all of the cards:

-- Round 1 --
Player 1's deck: 9, 2, 6, 3, 1
Player 2's deck: 5, 8, 4, 7, 10
Player 1 plays: 9
Player 2 plays: 5
Player 1 wins the round!

-- Round 2 --
Player 1's deck: 2, 6, 3, 1, 9, 5
Player 2's deck: 8, 4, 7, 10
Player 1 plays: 2
Player 2 plays: 8
Player 2 wins the round!

-- Round 3 --
Player 1's deck: 6, 3, 1, 9, 5
Player 2's deck: 4, 7, 10, 8, 2
Player 1 plays: 6
Player 2 plays: 4
Player 1 wins the round!

-- Round 4 --
Player 1's deck: 3, 1, 9, 5, 6, 4
Player 2's deck: 7, 10, 8, 2
Player 1 plays: 3
Player 2 plays: 7
Player 2 wins the round!

-- Round 5 --
Player 1's deck: 1, 9, 5, 6, 4
Player 2's deck: 10, 8, 2, 7, 3
Player 1 plays: 1
Player 2 plays: 10
Player 2 wins the round!

...several more rounds pass...

-- Round 27 --
Player 1's deck: 5, 4, 1
Player 2's deck: 8, 9, 7, 3, 2, 10, 6
Player 1 plays: 5
Player 2 plays: 8
Player 2 wins the round!

-- Round 28 --
Player 1's deck: 4, 1
Player 2's deck: 9, 7, 3, 2, 10, 6, 8, 5
Player 1 plays: 4
Player 2 plays: 9
Player 2 wins the round!

-- Round 29 --
Player 1's deck: 1
Player 2's deck: 7, 3, 2, 10, 6, 8, 5, 9, 4
Player 1 plays: 1
Player 2 plays: 7
Player 2 wins the round!


== Post-game results ==
Player 1's deck:
Player 2's deck: 3, 2, 10, 6, 8, 5, 9, 4, 7, 1

Once the game ends, you can calculate the winning player's score. The bottom card in their deck is worth the value of the card multiplied by 1, the second-from-the-bottom card is worth the value of the card multiplied by 2, and so on. With 10 cards, the top card is worth the value on the card multiplied by 10. In this example, the winning player's score is:

   3 * 10
+  2 *  9
+ 10 *  8
+  6 *  7
+  8 *  6
+  5 *  5
+  9 *  4
+  4 *  3
+  7 *  2
+  1 *  1
= 306

So, once the game ends, the winning player's score is 306.

Play the small crab in a game of Combat using the two decks you just dealt. What is the winning player's score?

Your puzzle answer was 33680.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

You lost to the small crab! Fortunately, crabs aren't very good at recursion. To defend your honor as a Raft Captain, you challenge the small crab to a game of Recursive Combat.

Recursive Combat still starts by splitting the cards into two decks (you offer to play with the same starting decks as before - it's only fair). Then, the game consists of a series of rounds with a few changes:

	Before either player deals a card, if there was a previous round in this game that had exactly the same cards in the same order in the same players' decks, the game instantly ends in a win for player 1. Previous rounds from other games are not considered. (This prevents infinite games of Recursive Combat, which everyone agrees is a bad idea.)
	Otherwise, this round's cards must be in a new configuration; the players begin the round by each drawing the top card of their deck as normal.
	If both players have at least as many cards remaining in their deck as the value of the card they just drew, the winner of the round is determined by playing a new game of Recursive Combat (see below).
	Otherwise, at least one player must not have enough cards left in their deck to recurse; the winner of the round is the player with the higher-value card.

As in regular Combat, the winner of the round (even if they won the round by winning a sub-game) takes the two cards dealt at the beginning of the round and places them on the bottom of their own deck (again so that the winner's card is above the other card). Note that the winner's card might be the lower-valued of the two cards if they won the round due to winning a sub-game. If collecting cards by winning the round causes a player to have all of the cards, they win, and the game ends.

Here is an example of a small game that would loop forever without the infinite game prevention rule:

Player 1:
43
19

Player 2:
2
29
14

During a round of Recursive Combat, if both players have at least as many cards in their own decks as the number on the card they just dealt, the winner of the round is determined by recursing into a sub-game of Recursive Combat. (For example, if player 1 draws the 3 card, and player 2 draws the 7 card, this would occur if player 1 has at least 3 cards left and player 2 has at least 7 cards left, not counting the 3 and 7 cards that were drawn.)

To play a sub-game of Recursive Combat, each player creates a new deck by making a copy of the next cards in their deck (the quantity of cards copied is equal to the number on the card they drew to trigger the sub-game). During this sub-game, the game that triggered it is on hold and completely unaffected; no cards are removed from players' decks to form the sub-game. (For example, if player 1 drew the 3 card, their deck in the sub-game would be copies of the next three cards in their deck.)

Here is a complete example of gameplay, where Game 1 is the primary game of Recursive Combat:

=== Game 1 ===

-- Round 1 (Game 1) --
Player 1's deck: 9, 2, 6, 3, 1
Player 2's deck: 5, 8, 4, 7, 10
Player 1 plays: 9
Player 2 plays: 5
Player 1 wins round 1 of game 1!

-- Round 2 (Game 1) --
Player 1's deck: 2, 6, 3, 1, 9, 5
Player 2's deck: 8, 4, 7, 10
Player 1 plays: 2
Player 2 plays: 8
Player 2 wins round 2 of game 1!

-- Round 3 (Game 1) --
Player 1's deck: 6, 3, 1, 9, 5
Player 2's deck: 4, 7, 10, 8, 2
Player 1 plays: 6
Player 2 plays: 4
Player 1 wins round 3 of game 1!

-- Round 4 (Game 1) --
Player 1's deck: 3, 1, 9, 5, 6, 4
Player 2's deck: 7, 10, 8, 2
Player 1 plays: 3
Player 2 plays: 7
Player 2 wins round 4 of game 1!

-- Round 5 (Game 1) --
Player 1's deck: 1, 9, 5, 6, 4
Player 2's deck: 10, 8, 2, 7, 3
Player 1 plays: 1
Player 2 plays: 10
Player 2 wins round 5 of game 1!

-- Round 6 (Game 1) --
Player 1's deck: 9, 5, 6, 4
Player 2's deck: 8, 2, 7, 3, 10, 1
Player 1 plays: 9
Player 2 plays: 8
Player 1 wins round 6 of game 1!

-- Round 7 (Game 1) --
Player 1's deck: 5, 6, 4, 9, 8
Player 2's deck: 2, 7, 3, 10, 1
Player 1 plays: 5
Player 2 plays: 2
Player 1 wins round 7 of game 1!

-- Round 8 (Game 1) --
Player 1's deck: 6, 4, 9, 8, 5, 2
Player 2's deck: 7, 3, 10, 1
Player 1 plays: 6
Player 2 plays: 7
Player 2 wins round 8 of game 1!

-- Round 9 (Game 1) --
Player 1's deck: 4, 9, 8, 5, 2
Player 2's deck: 3, 10, 1, 7, 6
Player 1 plays: 4
Player 2 plays: 3
Playing a sub-game to determine the winner...

=== Game 2 ===

-- Round 1 (Game 2) --
Player 1's deck: 9, 8, 5, 2
Player 2's deck: 10, 1, 7
Player 1 plays: 9
Player 2 plays: 10
Player 2 wins round 1 of game 2!

-- Round 2 (Game 2) --
Player 1's deck: 8, 5, 2
Player 2's deck: 1, 7, 10, 9
Player 1 plays: 8
Player 2 plays: 1
Player 1 wins round 2 of game 2!

-- Round 3 (Game 2) --
Player 1's deck: 5, 2, 8, 1
Player 2's deck: 7, 10, 9
Player 1 plays: 5
Player 2 plays: 7
Player 2 wins round 3 of game 2!

-- Round 4 (Game 2) --
Player 1's deck: 2, 8, 1
Player 2's deck: 10, 9, 7, 5
Player 1 plays: 2
Player 2 plays: 10
Player 2 wins round 4 of game 2!

-- Round 5 (Game 2) --
Player 1's deck: 8, 1
Player 2's deck: 9, 7, 5, 10, 2
Player 1 plays: 8
Player 2 plays: 9
Player 2 wins round 5 of game 2!

-- Round 6 (Game 2) --
Player 1's deck: 1
Player 2's deck: 7, 5, 10, 2, 9, 8
Player 1 plays: 1
Player 2 plays: 7
Player 2 wins round 6 of game 2!
The winner of game 2 is player 2!

...anyway, back to game 1.
Player 2 wins round 9 of game 1!

-- Round 10 (Game 1) --
Player 1's deck: 9, 8, 5, 2
Player 2's deck: 10, 1, 7, 6, 3, 4
Player 1 plays: 9
Player 2 plays: 10
Player 2 wins round 10 of game 1!

-- Round 11 (Game 1) --
Player 1's deck: 8, 5, 2
Player 2's deck: 1, 7, 6, 3, 4, 10, 9
Player 1 plays: 8
Player 2 plays: 1
Player 1 wins round 11 of game 1!

-- Round 12 (Game 1) --
Player 1's deck: 5, 2, 8, 1
Player 2's deck: 7, 6, 3, 4, 10, 9
Player 1 plays: 5
Player 2 plays: 7
Player 2 wins round 12 of game 1!

-- Round 13 (Game 1) --
Player 1's deck: 2, 8, 1
Player 2's deck: 6, 3, 4, 10, 9, 7, 5
Player 1 plays: 2
Player 2 plays: 6
Playing a sub-game to determine the winner...

=== Game 3 ===

-- Round 1 (Game 3) --
Player 1's deck: 8, 1
Player 2's deck: 3, 4, 10, 9, 7, 5
Player 1 plays: 8
Player 2 plays: 3
Player 1 wins round 1 of game 3!

-- Round 2 (Game 3) --
Player 1's deck: 1, 8, 3
Player 2's deck: 4, 10, 9, 7, 5
Player 1 plays: 1
Player 2 plays: 4
Playing a sub-game to determine the winner...

=== Game 4 ===

-- Round 1 (Game 4) --
Player 1's deck: 8
Player 2's deck: 10, 9, 7, 5
Player 1 plays: 8
Player 2 plays: 10
Player 2 wins round 1 of game 4!
The winner of game 4 is player 2!

...anyway, back to game 3.
Player 2 wins round 2 of game 3!

-- Round 3 (Game 3) --
Player 1's deck: 8, 3
Player 2's deck: 10, 9, 7, 5, 4, 1
Player 1 plays: 8
Player 2 plays: 10
Player 2 wins round 3 of game 3!

-- Round 4 (Game 3) --
Player 1's deck: 3
Player 2's deck: 9, 7, 5, 4, 1, 10, 8
Player 1 plays: 3
Player 2 plays: 9
Player 2 wins round 4 of game 3!
The winner of game 3 is player 2!

...anyway, back to game 1.
Player 2 wins round 13 of game 1!

-- Round 14 (Game 1) --
Player 1's deck: 8, 1
Player 2's deck: 3, 4, 10, 9, 7, 5, 6, 2
Player 1 plays: 8
Player 2 plays: 3
Player 1 wins round 14 of game 1!

-- Round 15 (Game 1) --
Player 1's deck: 1, 8, 3
Player 2's deck: 4, 10, 9, 7, 5, 6, 2
Player 1 plays: 1
Player 2 plays: 4
Playing a sub-game to determine the winner...

=== Game 5 ===

-- Round 1 (Game 5) --
Player 1's deck: 8
Player 2's deck: 10, 9, 7, 5
Player 1 plays: 8
Player 2 plays: 10
Player 2 wins round 1 of game 5!
The winner of game 5 is player 2!

...anyway, back to game 1.
Player 2 wins round 15 of game 1!

-- Round 16 (Game 1) --
Player 1's deck: 8, 3
Player 2's deck: 10, 9, 7, 5, 6, 2, 4, 1
Player 1 plays: 8
Player 2 plays: 10
Player 2 wins round 16 of game 1!

-- Round 17 (Game 1) --
Player 1's deck: 3
Player 2's deck: 9, 7, 5, 6, 2, 4, 1, 10, 8
Player 1 plays: 3
Player 2 plays: 9
Player 2 wins round 17 of game 1!
The winner of game 1 is player 2!


== Post-game results ==
Player 1's deck:
Player 2's deck: 7, 5, 6, 2, 4, 1, 10, 8, 9, 3

After the game, the winning player's score is calculated from the cards they have in their original deck using the same rules as regular Combat. In the above game, the winning player's score is 291.

Defend your honor as Raft Captain by playing the small crab in a game of Recursive Combat using the same two decks as before. What is the winning player's score?



'''

from collections import deque
import itertools

test_data_1 = [ 'Player 1:\n9\n2\n6\n3\n1', 'Player 2:\n5\n8\n4\n7\n10' ]
test_data_2 = [ 'Player 1:\n43\n19', 'Player 2:\n2\n29\n14' ]


def score_deck( deck ):
	point_value = 1
	score = 0

	for i in reversed( deck ):
		if DEBUG:
			print( '{} : {}'.format( i, i * point_value ) )
		score += i * point_value
		point_value += 1

	return score


def build_deck ( raw_data ):
	deck_1 = deque( [ int( x ) for x in raw_data[ 0 ].split( ':' )[ 1 ].split( ) ] )
	deck_2 = deque( [ int( x ) for x in raw_data[ 1 ].split( ':' )[ 1 ].split( ) ] )

	return deck_1, deck_2


def play_combat( raw_data ):
	score = 0
	turn = 1
	deck_1, deck_2 = build_deck( raw_data )

	while len( deck_1 ) != 0 or len( deck_2 ) != 0:
		if len( deck_1 ) == 0 or len( deck_2 ) == 0:
			print( '== Post-game results ==' )
			print( "Player 1's deck: {}".format( ", ".join( map( str, [ x for x in deck_1 ] ) ) ) )
			print( "Player 2's deck: {}\n".format( ", ".join( map( str, [ x for x in deck_2 ] ) ) ) )
			break
		else:
			print( '-- Round {} -- '.format( turn ) )
			print( "Player 1's deck: {}".format( ", ".join( map( str, [ x for x in deck_1 ] ) ) ) )
			print( "Player 2's deck: {}".format( ", ".join( map( str, [ x for x in deck_2 ] ) ) ) )
			print( 'Player 1 plays: {}\nPlayer 2 plays: {}'.format( deck_1[ 0 ], deck_2[ 0 ] ) )

		if deck_1[ 0 ] > deck_2[ 0 ]:
			print( 'Player 1 wins the round!\n' )
			deck_1.rotate( -1 )
			deck_1.append( deck_2.popleft( ) )
		else:
			deck_2.rotate( -1 )
			deck_2.append( deck_1.popleft( ) )
			print( 'Player 2 wins the round!\n' )

		turn += 1


	if len( deck_1 ) > len( deck_2 ):
		score = score_deck( deck_1 )

	else:
		score = score_deck( deck_2 )

	print( '\nFinal score: {}'.format( score ) )
	return score


def play_recursive_combat( raw_data, game, deck_1 = None, deck_2 = None ):

	score = 0
	turn = 1
	winner = 0

	if not deck_1 and not deck_2:
		deck_1, deck_2 = build_deck( raw_data )
	else:
		previous_deck_1 = deck_1
		previous_deck_2 = deck_2

	decks = [ deck_1, deck_2 ]

	previous_deck_1 = set( )
	previous_deck_2 = set( )

	prev_card_1 = 0
	prev_card_2 = 0
	the_pot = [ ]

	if DEBUG:
		print( '=== Game {} ==='.format( game ) )
	while len( deck_1 ) > 0 and len( deck_2 ) > 0:
		prev_card_1 = deck_1[ 0 ]
		prev_card_2 = deck_2[ 0 ]

		if DEBUG:
			if len( deck_1 ) == 0 or len( deck_2 ) == 0:
				print( '== Post-game results ==' )
				print( "Player 1's deck: {}".format( ", ".join( map( str, [ x for x in deck_1 ] ) ) ) )
				print( "Player 2's deck: {}\n".format( ", ".join( map( str, [ x for x in deck_2 ] ) ) ) )
				break
			else:
				print( '\n-- Round {} (Game {}) -- '.format( turn, game ) )
				print( "Player 1's deck: {}".format( ", ".join( map( str, [ x for x in deck_1 ] ) ) ) )
				print( "Player 2's deck: {}".format( ", ".join( map( str, [ x for x in deck_2 ] ) ) ) )
				print( 'Player 1 plays: {}\nPlayer 2 plays: {}'.format( deck_1[ 0 ], deck_2[ 0 ] ) )


		# if deck_1 != previous_deck_1 and deck_2 != previous_deck_2:
			# print( 'Player 1 wins round {} of game {}!\n'.format( turn, game ) )
			# deck_1.rotate( -1 )
			# deck_1.append( deck_2.popleft( ) )

		# elif deck_1[ 0 ] > deck_2[ 0 ]:
			# print( 'Player 1 wins round {} of game {}!\n'.format( turn, game ) )
			# deck_1.rotate( -1 )
			# deck_1.append( deck_2.popleft( ) )

		# elif deck_1[ 0 ] < deck_2[ 0 ]:
			# deck_2.rotate( -1 )
			# deck_2.append( deck_1.popleft( ) )
			# print( 'Player 2 wins round {} of game {}!\n'.format( turn, game ) )

		if tuple( deck_1 ) in previous_deck_1 and tuple( deck_2 ) in previous_deck_2:
			winner = 0
			break

		elif deck_1[ 0 ] > deck_2[ 0 ]:
			previous_deck_1.add( tuple( deck_1 ) )
			previous_deck_2.add( tuple( deck_2 ) )

			winner = 0
			the_pot.append( deck_1.popleft( ) )
			the_pot.append( deck_2.popleft( ) )

		elif deck_1[ 0 ] < deck_2[ 0 ]:
			previous_deck_1.add( tuple( deck_1 ) )
			previous_deck_2.add( tuple( deck_2 ) )

			winner = 1
			the_pot.append( deck_2.popleft( ) )
			the_pot.append( deck_1.popleft( ) )

		# if len( deck_1 ) >= deck_1[ 0 ] and len( deck_2  ) >= deck_2[ 0 ]:
			# score, winner = play_recursive_combat( raw_data, game + 1, deck_1 = deck_1, deck_2 = deck_2 )

			# if winner == 0:
				# the_pot.append( deck_2.popleft( ) )
				# the_pot.append( deck_1.popleft( ) )

			# else:
				# the_pot.append( deck_1.popleft( ) )
				# the_pot.append( deck_2.popleft( ) )

		if len( deck_1 ) >= prev_card_1 and len( deck_2 ) >= prev_card_2:
			if DEBUG:
				print( 'Playing a sub-game to determine the winner...\n'.format( game + 1 ) )

			card_1 = deque( )
			card_2 = deque( )

			# F. Unroll the pot.
			if winner == 0:
				card_1 = the_pot[ 0 ]
				card_2 = the_pot[ 1 ]
			else:
				card_1 = the_pot[ 1 ]
				card_2 = the_pot[ 0 ]
			the_pot = [ ]

			new_deck_1 = deque( itertools.islice( deck_1, 0, prev_card_1 ) )
			new_deck_2 = deque( itertools.islice( deck_2, 0, prev_card_2 ) )
			score, winner = play_recursive_combat( raw_data, game + 1, deck_1 = new_deck_1, deck_2 = new_deck_2 )

			if winner == 0:
				the_pot.append( card_1 )
				the_pot.append( card_2 )
			else:
				the_pot.append( card_2 )
				the_pot.append( card_1 )

			if DEBUG:
				print( '\n...anyway, back to game {}.'.format( game ) )

			# if winner == 0:
				# deck_1.extend( the_pot )
			# elif winner == 1:
				# deck_2.extend( the_pot )
		if DEBUG:
			print( 'Player {} wins round {} of game {}!'.format( winner + 1, turn, game ) )

		if winner == 0:
			deck_1.extend( the_pot )
		elif winner == 1:
			deck_2.extend( the_pot )


		the_pot = [ ]
		turn += 1


	if len( deck_1 ) > len( deck_2 ):
		score = score_deck( deck_1 )
		winner = 0

	else:
		score = score_deck( deck_2 )
		winner = 1

	if DEBUG:
		print( 'The winner of game {} is player {}!'.format( game, winner + 1 ) )
		print( '== Post-game results ==' )
		print( "Player 1's deck: {}".format( ", ".join( map( str, [ x for x in deck_1 ] ) ) ) )
		print( "Player 2's deck: {}\n".format( ", ".join( map( str, [ x for x in deck_2 ] ) ) ) )
	return score, winner



DEBUG = True
if __name__ == "__main__":
	input = r'D:\Projects\Python\Personal\Advent_of_Code\2020\day_22_input.txt'
	# input = r'D:\Dropbox\Projects\Python\Advent_of_Code\2020\day_22_input.txt'

	with open( input, 'r' ) as input_file:
		raw_data = input_file.read( ).split( '\n\n' )

	# play_combat( raw_data )
	score, winner = play_recursive_combat( raw_data, 1 )

	print( "The winning player's score is: {}".format( score ) )