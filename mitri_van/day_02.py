'''
--- Day 2: Password Philosophy ---

Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

	1-3 a: abcde
	1-3 b: cdefg
	2-9 c: ccccccccc

Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?

Your puzzle answer was 515.

--- Part Two ---

While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

	1-3 a: abcde is valid: position 1 contains a and position 3 does not.
	1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
	2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

How many passwords are valid according to the new interpretation of the policies?

Your puzzle answer was 711.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

def check_password_alpha( entry ):
	valid_hits, crypto_key = get_password_policy( entry[ 0 ] )
	password = entry[ 1 ].split( )[ 0 ]
	hits = password.count( crypto_key )

	if valid_hits[ 0 ] <= hits:
		if hits <= valid_hits[ 1 ]:
			return True

	return False

def check_password_beta( entry ):
	is_valid = False

	valid_positions, crypto_key = get_password_policy( entry[ 0 ] )
	password = entry[ 1 ].lstrip( ).split( )[ 0 ]

	for idx in valid_positions:
		relative_idx = idx - 1

		if relative_idx > len( password ):
			is_valid = False

		else:
			if password[ relative_idx ] == crypto_key:
				is_valid = not is_valid

	return is_valid


def get_password_policy( entry ):
	entry_bits = entry.split( )
	key = entry_bits[ 1 ]

	pwd_criteria = entry_bits[ 0 ].split( '-' )
	valid_range = ( int( pwd_criteria[ 0 ] ), int( pwd_criteria[ 1 ] ) )

	return ( valid_range, key )


if __name__ == "__main__":
	check_policy_one = False
	result = False

	input = r'D:\Projects\Python\Personal\Advent_of_Code\2020\day_02_input.txt'
	# input = r'D:\Dropbox\Projects\Python\Advent_of_Code\2020\day_02_input.txt'

	data = [ ]

	with open( input, 'r' ) as input_file:
		data = [ x.strip( ).split( ':' ) for x in input_file.readlines( ) ]

	valid_passwords = [ ]
	invalid_passwords = [ ]

	for datum in data:
		if check_policy_one:
			result = check_password_alpha( datum )
		else:
			result = check_password_beta( datum )

		if result:
			valid_passwords.append( datum )

		else:
			invalid_passwords.append( datum )

	print( 'Valid passwords:\t\t{0}\nInvalid passwords: \t{1}'.format( len( valid_passwords ), len( invalid_passwords ) ) )