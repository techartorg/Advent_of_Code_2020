'''
--- Day 7: Handy Haversacks ---

You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to grab some food: all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible for these regulations considered how long they would take to enforce!

For example, consider the following rules:

	light red bags contain 1 bright white bag, 2 muted yellow bags.
	dark orange bags contain 3 bright white bags, 4 muted yellow bags.
	bright white bags contain 1 shiny gold bag.
	muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
	shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
	dark olive bags contain 3 faded blue bags, 4 dotted black bags.
	vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
	faded blue bags contain no other bags.
	dotted black bags contain no other bags.

# These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

	A bright white bag, which can hold your shiny gold bag directly.
	A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
	A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
	A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.

So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you get all of it.)

Your puzzle answer was 148.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

	faded blue bags contain 0 other bags.
	dotted black bags contain 0 other bags.
	vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
	dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.

So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.

In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?

Your puzzle answer was 24867.

Both parts of this puzzle are complete! They provide two gold stars: **

'''

import regex
obj_regex = regex.compile( r' bag{0,1}[s,. ]+', regex.I )
contents_regex = regex.compile( r'(\d+) ', regex.I )

test_data = [ 'light red bags contain 1 bright white bag, 2 muted yellow bags.',
				  'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
				  'bright white bags contain 1 shiny gold bag.',
				  'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
				  'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
				  'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
				  'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
				  'faded blue bags contain no other bags.',
				  'dotted black bags contain no other bags.' ]



class Bag( ):
	def __init__( self, name ):
		self.name = name
		self.contents = { }


	def __repr__( self ):
		return 'Bag_' + self.name.replace( ' ', '_' )


	def has_color( self, color ):
		for bag in self.contents.keys( ):
			if bag != 'None' and bag.name == color:
				return True

		return False


def can_contain_color( bags, color ):
	count = 0
	valid_bags = [ ]

	for bag in bags:
		if bag.has_color( color ):
			count += 1
			valid_bags.append( bag )

	return count, valid_bags


def find_all_bags( data, color ):
	total_bags = 0
	total_bag_colors = [ ]

	num_bags, bag_colors = can_contain_color( data, color )
	total_bag_colors = total_bag_colors = bag_colors

	sub_total_bags = 0
	for bag in bag_colors:
		sub_total_bags, bag_colors = can_contain_color( data, bag.name )
		total_bags += sub_total_bags
		total_bag_colors += bag_colors

	return list( set( total_bag_colors ) )


def find_num_bags( all_bags, bag_color ):
	total_bags = 0
	my_bag = [ bag for bag in all_bags if bag.name == bag_color ][ 0 ]

	for bag in my_bag.contents.keys( ):
		if bag == 'None':
			return total_bags

		num = 1
		bag_multiplier = my_bag.contents[ bag ]
		if bag_multiplier != 0:
			num += find_num_bags( all_bags, bag.name )
			total_bags += num * bag_multiplier

		else:
			return num

	return total_bags


def get_contents( data ):
	items = [ ]
	inventory = obj_regex.split( data )

	for things in inventory[ :-1 ]:
		bag = contents_regex.split( things )
		if bag[ 0 ] == 'no other':
			return [ ( 0, 'None' ) ]
		else:
			quantity = int( bag[ 1 ] )
			new_bag = Bag( bag[ 2 ] )
			items.append( ( quantity, new_bag ) )

	return items


def parse_data( data ):
	all_bags = [ ]
	bag = ''
	contents = ''

	for line in data:
		bag = Bag( line[ 0 ] )
		items = get_contents( line[ 1 ] )

		if items:
			for item in items:
				bag.contents[ item[ 1 ] ] = item[ 0 ]
		all_bags.append( bag )

	return all_bags


if __name__ == "__main__":
	input = r'D:\Projects\Python\Personal\Advent_of_Code\2020\day_07_input.txt'
	# input = r'D:\Dropbox\Projects\Python\Advent_of_Code\2020\day_07_input.txt'

	data = [ ]

	with open( input, 'r' ) as input_file:
		data = [ line.strip( ).split( ' bags contain ' ) for line in input_file.readlines( ) ]

	all_bags = parse_data( data )

	bag_color = 'shiny gold'
	num_bag_colors = find_all_bags( all_bags, bag_color )
	num_bags = find_num_bags( all_bags, bag_color )

	print( '\nNumber of bags that can contain a {0} bag: {1}'.format( bag_color, len( num_bag_colors ) ) )
	print( '\nNumber of bags inside a {0} bag: {1}'.format( bag_color, num_bags ) )
