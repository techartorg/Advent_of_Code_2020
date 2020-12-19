'''
--- Day 16: Ticket Translation ---
As you're walking to yet another connecting flight, you realize that one of the legs of your re-routed trip coming up is on a high-speed train. However, the train ticket you were given is in a language you don't understand. You should probably figure out what it says before you get to the train station after the next flight.

Unfortunately, you can't actually read the words on the ticket. You can, however, read the numbers, and so you figure out the fields these tickets must have and the valid ranges for values in those fields.

You collect the rules for ticket fields, the numbers on your ticket, and the numbers on other nearby tickets for the same train service (via the airport security cameras) together into a single document you can reference (your puzzle input).

The rules for ticket fields specify a list of fields that exist somewhere on the ticket and the valid ranges of values for each field. For example, a rule like class: 1-3 or 5-7 means that one of the fields in every ticket is named class and can be any value in the ranges 1-3 or 5-7 (inclusive, such that 3 and 5 are both valid in this field, but 4 is not).

Each ticket is represented by a single line of comma-separated values. The values are the numbers on the ticket in the order they appear; every ticket has the same format. For example, consider this ticket:

.--------------------------------------------------------.
| ????: 101    ?????: 102   ??????????: 103     ???: 104 |
|                                                        |
| ??: 301  ??: 302             ???????: 303      ??????? |
| ??: 401  ??: 402           ???? ????: 403    ????????? |
'--------------------------------------------------------'
Here, ? represents text in a language you don't understand. This ticket might be represented as 101,102,103,104,301,302,303,401,402,403; of course, the actual train tickets you're looking at are much more complicated. In any case, you've extracted just the numbers in such a way that the first number is always the same specific field, the second number is always a different specific field, and so on - you just don't know what each position actually means!

Start by determining which tickets are completely invalid; these are tickets that contain values which aren't valid for any field. Ignore your ticket for now.

For example, suppose you have the following notes:

class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12

It doesn't matter which position corresponds to which field; you can identify invalid nearby tickets by considering only whether tickets contain values that are not valid for any field. In this example, the values on the first nearby ticket are all valid for at least one field. This is not true of the other three nearby tickets: the values 4, 55, and 12 are are not valid for any field. Adding together all of the invalid values produces your ticket scanning error rate: 4 + 55 + 12 = 71.

Consider the validity of the nearby tickets you scanned. What is your ticket scanning error rate?

Your puzzle answer was 27911.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

Now that you've identified which tickets contain invalid values, discard those tickets entirely. Use the remaining valid tickets to determine which field is which.

Using the valid ranges for each field, determine what order the fields appear on the tickets. The order is consistent between all tickets: if seat is the third field, it is the third field on every ticket, including your ticket.

For example, suppose you have the following notes:

class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9

Based on the nearby tickets in the above example, the first position must be row, the second position must be class, and the third position must be seat; you can conclude that in your ticket, class is 12, row is 11, and seat is 13.

Once you work out which field is which, look for the six fields on your ticket that start with the word departure. What do you get if you multiply those six values together?

Your puzzle answer was 737176602479.

Both parts of this puzzle are complete! They provide two gold stars: **

'''
from functools import reduce

test_data_1 = [ 'class: 1-3 or 5-7\nrow: 6-11 or 33-44\nseat: 13-40 or 45-50',
				  'your ticket:\n7,1,14',
				  'nearby tickets:\n7,3,47\n40,4,50\n55,2,20\n38,6,12\n' ]

test_data_2 = [ 'class: 0-1 or 4-19\nrow: 0-5 or 8-19\nseat: 0-13 or 16-19',
					 'your ticket:\n11,12,13',
					 'nearby tickets:\n3,9,18\n15,1,5\n5,14,9' ]


def parse_rules( data_input ):
	rule_sets = { }
	results = set( )

	for x in data_input:
		rule_type = x.split( ': ' )[ 0 ]
		rules = x.split( ': ' )[ 1 ].split( ' or ' )
		rule_sets[ rule_type ] = set( )
		for rule in rules:
			sub_rule = [ list( map( int, num_str.split( '-' ) ) ) for num_str in rule.split( ', ' ) ][ 0 ]
			result = list( range( sub_rule[ 0 ], sub_rule[ -1 ] + 1 ) )
			[ results.add( x ) for x in result ]
			[ rule_sets[ rule_type ].add( x ) for x in result ]

	return list( results ), rule_sets


def validate_tickets( rules, tickets ):
	error_rate = [ ]
	valid_tickets = [ ]

	for ticket in tickets:
		invalid_hits = [ x for x in ticket if x not in rules ]
		if invalid_hits:
			error_rate.append( reduce( ( lambda x, y: x + y ), invalid_hits ) )
		else:
			valid_tickets.append( ticket )

	return error_rate, valid_tickets


def decrypt_ticket_fields( decryption_key ):
	decrypted_fields = { }

	while decryption_key:
		unique_fields = [ x for x in decryption_key if len( decryption_key[ x ] ) == 1 ]
		for entry in unique_fields:
			decrypted_fields[ entry ] = decryption_key.pop( entry )[ 0 ]
			[ decryption_key[ x ].remove( decrypted_fields[ entry ] ) for x in decryption_key ]

	return decrypted_fields


def decode_rules( rule_sets, tickets ):
	decryption_key = { }
	data_sets = { }

	for x in range( len( tickets[ 0 ] ) ):
		data_sets[ x ] = set( )

		for ticket in tickets:
			assert len( ticket ) <= 20, "Ticket has more than 20 entries"
			data_sets[ x ].add( ticket[ x ] )

	for r_key in rule_sets:
		decryption_key[ r_key ] = [ ]
		for data_set in data_sets:
			# output = '{0} : {1}\t\t{2}'.format( r_key, data_set, data_sets[ data_set ] )
			# output = '{0} : {1}'.format( data_set, r_key )
			if rule_sets[ r_key ].issuperset( data_sets[ data_set ] ):
				decryption_key[ r_key ].append( data_set )
				# output += '\t\t------ is superset'
			# print( output )

	decrypted_fields = decrypt_ticket_fields( decryption_key )

	return decrypted_fields

def math_fields( decrypted_fields, ticket ):
	math_it = [ ]

	for x in decrypted_fields:
		if 'departure' in x:
			math_it.append( ticket[ decrypted_fields[ x ] ] )

	return reduce( ( lambda x, y: x * y ), math_it )


def scan_tickets( raw_data, error_rate = True ):
	rule_list = raw_data[ 0 ].strip( '\n' ).split( '\n' )
	ticket = [ int( x ) for x in raw_data[ 1 ].split( '\n' )[ 1 ].split( ',' ) ]
	nearby_tickets = [ [ int( num ) for num in ticket.split( ',' ) ] for ticket in raw_data[ 2 ].split( ':\n' )[ 1 ].strip( ).split( '\n' ) ]

	rules, rule_sets = parse_rules( rule_list )
	error_rate, valid_tickets = validate_tickets( rules, nearby_tickets )

	decrypted_fields = decode_rules( rule_sets, valid_tickets )
	output = math_fields( decrypted_fields, ticket )

	return error_rate, output


if __name__ == "__main__":
	input = r'D:\Projects\Python\Personal\Advent_of_Code\2020\day_16_input.txt'
	# input = r'D:\Dropbox\Projects\Python\Advent_of_Code\2020\day_16_input.txt'

	with open( input, 'r' ) as input_file:
		raw_data = input_file.read( ).split( '\n\n' )

	error_rate, output = scan_tickets( raw_data )
	print( 'The ticket scanning error rate is: {0}'.format( sum( error_rate ) ) )
	print( 'Output: {0}'.format( output ) )
