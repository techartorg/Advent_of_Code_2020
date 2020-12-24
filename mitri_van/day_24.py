'''
--- Day 24: Lobby Layout ---

Your raft makes it to the tropical island; it turns out that the small crab was an excellent navigator. You make your way to the resort.

As you enter the lobby, you discover a small problem: the floor is being renovated. You can't even reach the check-in desk until they've finished installing the new tile floor.

The tiles are all hexagonal; they need to be arranged in a hex grid with a very specific color pattern. Not in the mood to wait, you offer to help figure out the pattern.

The tiles are all white on one side and black on the other. They start with the white side facing up. The lobby is large enough to fit whatever pattern might need to appear there.

A member of the renovation crew gives you a list of the tiles that need to be flipped over (your puzzle input). Each line in the list identifies a single tile that needs to be flipped by giving a series of steps starting from a reference tile in the very center of the room. (Every line starts from the same reference tile.)

Because the tiles are hexagonal, every tile has six neighbors: east, southeast, southwest, west, northwest, and northeast. These directions are given in your list, respectively, as e, se, sw, w, nw, and ne. A tile is identified by a series of these directions with no delimiters; for example, esenee identifies the tile you land on if you start at the reference tile and then move one tile east, one tile southeast, one tile northeast, and one tile east.

Each time a tile is identified, it flips from white to black or from black to white. Tiles might be flipped more than once. For example, a line like esew flips a tile immediately adjacent to the reference tile, and a line like nwwswee flips the reference tile itself.

Here is a larger example:

sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew

In the above example, 10 tiles are flipped once (to black), and 5 more are flipped twice (to black, then back to white). After all of these instructions have been followed, a total of 10 tiles are black.

Go through the renovation crew's list and determine which tiles they need to flip. After all of the instructions have been followed, how many tiles are left with the black side up?

Your puzzle answer was 282.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

The tile floor in the lobby is meant to be a living art exhibit. Every day, the tiles are all flipped according to the following rules:

    Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
    Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.

Here, tiles immediately adjacent means the six tiles directly touching the tile in question.

The rules are applied simultaneously to every tile; put another way, it is first determined which tiles need to be flipped, then they are all flipped at the same time.

In the above example, the number of black tiles that are facing up after the given number of days has passed is as follows:

Day 1: 15
Day 2: 12
Day 3: 25
Day 4: 14
Day 5: 23
Day 6: 28
Day 7: 41
Day 8: 37
Day 9: 49
Day 10: 37

Day 20: 132
Day 30: 259
Day 40: 406
Day 50: 566
Day 60: 788
Day 70: 1106
Day 80: 1373
Day 90: 1844
Day 100: 2208

After executing this process a total of 100 times, there would be 2208 black tiles facing up.

How many tiles will be black after 100 days?

'''
from collections import deque
import re

dir_regex = re.compile( r'(?<!=[ns])w|(?<!=[ns])e|ne|nw|se|sw', re.I )

test_data_1 = ['sesenwnenenewseeswwswswwnenewsewsw',
					'neeenesenwnwwswnenewnwwsewnenwseswesw',
					'seswneswswsenwwnwse',
					'nwnwneseeswswnenewneswwnewseswneseene',
					'swweswneswnenwsewnwneneseenw',
					'eesenwseswswnenwswnwnwsewwnwsene',
					'sewnenenenesenwsewnenwwwse',
					'wenwwweseeeweswwwnwwe',
					'wsweesenenewnwwnwsenewsenwwsesesenwne',
					'neeswseenwwswnwswswnw',
					'nenwswwsewswnenenewsenwsenwnesesenew',
					'enewnwewneswsewnwswenweswnenwsenwsw',
					'sweneswneswneneenwnewenewwneswswnese',
					'swwesenesewenwneswnwwneseswwne',
					'enesenwswwswneneswsenwnewswseenwsese',
					'wnwnesenesenenwwnenwsewesewsesesew',
					'nenewswnwewswnenesenwnesewesw',
					'eneswnwswnwsenenwnwnwwseeswneewsenese',
					'neswnwewnwnwseenwseesewsenwsweewe',
					'wseweeenwnesenwwwswnew' ]



class Tile( ):

	def __init__( self, x, y, z, is_black = False):
		self.x = x
		self.y = y
		self.z = z
		self.is_black = is_black


	def __cmp__( self, other ):
		return ( self.x, self.y, self.z )


	def __eq__( self, other ):
		if type( other ) == tuple:
			if ( self.x, self.y, self.z ) == other:
				return True

		elif self.x == other.x and self.y == other.y and self.z == other.z:
			return True

		return False

	def __ne__( self, other ):
		if self.x != other.x and self.y != other.y and self.z != other.z:
			return True

		return False

	def __repr__( self ):
		if self.is_black:
			return 'Tile_b_({},{},{})'.format( self.x, self.y, self.z )
		return 'Tile_W_({},{},{})'.format( self.x, self.y, self.z )


	def flip( self ):
		self.is_black = not self.is_black

def parse_move( moves ):
	x = 0
	y = 0
	z = 0

	for move in moves:
		if move == 'n':
			# x += 0
			y += 1
			z += 1
		elif move == 'ne':
			x += 1
			# y += 0
			z += 1
		elif move == 'e':
			x += 2
			y -= 1
			z += 1
		elif move == 'se':
			x += 1
			y -= 1
			# z += 0
		elif move == 's':
			# x += 0
			y -= 1
			z -= 1
		elif move == 'sw':
			x -= 1
			# y += 0
			z -= 1
		elif move == 'w':
			x -= 2
			y += 1
			z -= 1
		elif move == 'nw':
			x -= 1
			y += 1
			# z += 0

	return x, y, z


def parse_data( data ):
	for datum in data:
		if datum != '':
			moves = dir_regex.findall( datum )
			x, y, z = parse_move( moves )
			# print( '\n{}'.format( moves ) )

			new_tile = Tile( x, y, z,  is_black = True )
			if new_tile not in tiles:
				tiles.append( new_tile )
				# print( new_tile )
			else:
				idx = tiles.index( new_tile )
				tiles[ idx ].flip( )
				# print( '\t\t\tFLIP: {}'.format( tiles[ idx ] ) )

	black_tiles = [ x for x in tiles if x.is_black ]

	if DEBUG:
		print( '{}\nThere are {} black tiles.'.format( tiles, len( black_tiles ) ) )
	print( '\nThere are {} black tiles.'.format( len( black_tiles ) ) )


def flip_daily_tiles( ):
	search_vectors = [ ( 0, 1, 1 ), ( 1, 0, 1 ), ( 1, -1, 0 ),
							 ( 0, -1, -1 ), ( -1, 0, -1 ), ( -1, 1, 0 ) ]
	flip_black = [ ]
	flip_white = [ ]

	for tile in tiles:
		neighbors = [ ]
		for vector in search_vectors:
			target = tuple( [ x + y for x, y in zip( (tile.x, tile.y, tile.z ), vector ) ] )
			if target in tiles:
				found_idx = tiles.index( target )
				neighbors.append( tiles[ found_idx ] )

		if DEBUG:
			print( '*********************************************\nTile: {}\nNeighbors: {}'.format( tile, neighbors ) )
		black_tiles = [ x for x in neighbors if x.is_black ]
		if len( black_tiles ) == 0 or len( black_tiles ) > 2:
			if tile.is_black:
				flip_white.append( tile )

		if not tile.is_black and len( black_tiles ) == 2:
			if not tile.is_black:
				flip_black.append( tile )

		if DEBUG:
			print( '\nFlip to white:\n{}'.format( flip_white ) )
			print( '-------------\nFlip to black: \n{}'.format( flip_black ) )

	for x in flip_black:
		x.is_black = True

	for x in flip_white:
		x.is_black = False

	black_tiles = [ x for x in tiles if x.is_black ]
	print( '\nThere are {} black tiles facing up.'.format( len( black_tiles ) ) )


tiles = [ ]
DEBUG = True
if __name__ == "__main__":
	input = r'D:\Projects\Python\Personal\Advent_of_Code\2020\day_24_input.txt'
	# input = r'D:\Dropbox\Projects\Python\Advent_of_Code\2020\day_24_input.txt'

	with open( input, 'r' ) as input_file:
		raw_data = input_file.read( ).split( '\n' )

	parse_data( test_data_1 )

	days = 1
	for i in range( 0, days ):
		flip_daily_tiles( )


