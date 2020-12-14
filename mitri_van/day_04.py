'''
--- Day 4: Passport Processing ---

You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport. While these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore aren't actually valid documentation for travel in most of the world.

It seems like you're not the only one having problems, though; a very long line has formed for the automatic passport scanners, and the delay could upset your travel itinerary.

Due to some questionable network security, you realize you might be able to solve both of these problems at the same time.

The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:

	byr (Birth Year)
	iyr (Issue Year)
	eyr (Expiration Year)
	hgt (Height)
	hcl (Hair Color)
	ecl (Eye Color)
	pid (Passport ID)
	cid (Country ID)

Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value pairs separated by spaces or newlines. Passports are separated by blank lines.

Here is an example batch file containing four passports:

	ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
	byr:1937 iyr:2017 cid:147 hgt:183cm

	iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
	hcl:#cfa07d byr:1929

	hcl:#ae17e1 iyr:2013
	eyr:2024
	ecl:brn pid:760753108 byr:1931
	hgt:179cm

	hcl:#cfa07d eyr:2025 pid:166559648
	iyr:2011 ecl:brn hgt:59in

The first passport is valid - all eight fields are present. The second passport is invalid - it is missing hgt (the Height field).

The third passport is interesting; the only missing field is cid, so it looks like data from North Pole Credentials, not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing cid fields. Treat this "passport" as valid.

The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not, so this passport is invalid.

According to the above rules, your improved system would report 2 valid passports.

Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?

Your puzzle answer was 216.

--- Part Two ---

The line is moving more quickly now, but you overhear airport security talking about how passports with invalid data are getting through. Better add some data validation, quick!

You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:

	byr (Birth Year) - four digits; at least 1920 and at most 2002.
	iyr (Issue Year) - four digits; at least 2010 and at most 2020.
	eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
	hgt (Height) - a number followed by either cm or in:
		If cm, the number must be at least 150 and at most 193.
		If in, the number must be at least 59 and at most 76.
	hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
	ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
	pid (Passport ID) - a nine-digit number, including leading zeroes.
	cid (Country ID) - ignored, missing or not.

Your job is to count the passports where all required fields are both present and valid according to the above rules. Here are some example values:

	byr valid:   2002
	byr invalid: 2003

	hgt valid:   60in
	hgt valid:   190cm
	hgt invalid: 190in
	hgt invalid: 190

	hcl valid:   #123abc
	hcl invalid: #123abz
	hcl invalid: 123abc

	ecl valid:   brn
	ecl invalid: wat

	pid valid:   000000001
	pid invalid: 0123456789

Here are some invalid passports:

	eyr:1972 cid:100
	hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

	iyr:2019
	hcl:#602927 eyr:1967 hgt:170cm
	ecl:grn pid:012533040 byr:1946

	hcl:dab227 iyr:2012
	ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

	hgt:59cm ecl:zzz
	eyr:2038 hcl:74454a iyr:2023
	pid:3556412378 byr:2007

Here are some valid passports:

	pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
	hcl:#623a2f

	eyr:2029 ecl:blu cid:129 byr:1989
	iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

	hcl:#888785
	hgt:164cm byr:2001 iyr:2015 cid:88
	pid:545766238 ecl:hzl
	eyr:2022

	iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719

Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as optional. In your batch file, how many passports are valid?

Your puzzle answer was 150.

Both parts of this puzzle are complete! They provide two gold stars: **'''

import ast


test_data = [ 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\n',
				  'byr:1937 iyr:2017 cid:147 hgt:183cm\n',
				  '\n',
				  'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\n',
				  'hcl:#cfa07d byr:1929\n',
				  '\n',
				  'hcl:#ae17e1 iyr:2013\n',
				  'eyr:2024\n',
				  'ecl:brn pid:760753108 byr:1931\n',
				  'hgt:179cm\n',
				  '\n',
				  'hcl:#cfa07d eyr:2025 pid:166559648\n',
				  'iyr:2011 ecl:brn hgt:59in\n' ]

test_data2 = [ 'eyr:1972 cid:100\n',
					'hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926\n',
					'\n',
					'iyr:2019\n',
					'hcl:#602927 eyr:1967 hgt:170cm\n',
					'ecl:grn pid:012533040 byr:1946\n',
					'\n',
					'hcl:dab227 iyr:2012\n',
					'ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277\n',
					'\n',
					'hgt:59cm ecl:zzz\n',
					'eyr:2038 hcl:74454a iyr:2023\n',
					'pid:3556412378 byr:2007\n' ]

test_data3 = [ 'pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980\n',
					'hcl:#623a2f\n',
					'\n',
					'eyr:2029 ecl:blu cid:129 byr:1989\n',
					'iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm\n',
					'\n',
					'hcl:#888785\n',
					'hgt:164cm byr:2001 iyr:2015 cid:88\n',
					'pid:545766238 ecl:hzl\n',
					'eyr:2022\n',
					'\n',
					'iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719\n' ]

BYR = 'byr'
IYR = 'iyr'
EYR = 'eyr'
HGT = 'hgt'
HCL = 'hcl'
ECL = 'ecl'
PID = 'pid'
CID = 'cid'

passport_fields = [ BYR, IYR, EYR, HGT, HCL, ECL, PID, CID ]


class Passport_Entry( ):
	def __init__( self, byr, iyr, eyr, hgt, hcl, ecl, pid, cid = None ):
		self.byr = byr
		self.iyr = iyr
		self.eyr = eyr
		self.hgt = hgt
		self.hcl = hcl
		self.ecl = ecl
		self.pid = pid
		self.cid = cid

	def __repr__( self ):
		return repr( 'Passport_Entry( ): byr: {0}  iyr: {1}  eyr: {2}  hgt: {3}  hcl: {4}  ecl: {5}  pid: {6}  cid: {7}'.format(
			self.byr, self.iyr, self.eyr, self.hgt, self.hcl, self.ecl, self.pid, self.cid ) )


def verify_data( passport_entry, expanded_check = True ):
	result = True
	missing_fields = [ ]
	invalid_fields = [ ]

	for field in passport_fields:
		if field not in passport_entry.keys( ):
			missing_fields.append( field )

			if field != 'cid':
				result = False

		if expanded_check and field not in missing_fields:
			if field == BYR:
				if int( passport_entry[ BYR ] ) not in range( 1920, 2003 ):
					result = False
					invalid_fields.append( BYR )

			if field == IYR:
				if int( passport_entry[ IYR ] ) not in range( 2010, 2021 ):
					result = False
					invalid_fields.append( IYR )

			if field == EYR:
				if int( passport_entry[ EYR ] ) not in range( 2020, 2031 ):
					result = False
					invalid_fields.append( EYR )

			if field == HGT:
				height = passport_entry[ HGT ]
				height_val = 0
				if 'cm' in height:
					height_val = int( height.split( 'cm' )[ 0 ] )
					if int( height_val ) not in range( 150, 194 ):
						result = False
						invalid_fields.append( HGT )

				elif 'in' in height:
					height_val = int( height.split( 'in' )[ 0 ] )
					if int( height_val ) not in range( 59, 77 ):
						result = False
						invalid_fields.append( HGT )

				else:
					result = False
					invalid_fields.append( HGT )

			if field == HCL:
				hair_col = passport_entry[ HCL ].split( '#' )

				if len( hair_col ) == 2:
					hair_val = hair_col[ 1 ]
					if len( hair_val ) == 6:
						if int( hair_val, 16 ):
							pass
				else:
					result = False
					invalid_fields.append( HCL )

			if field == ECL:
				eye_colors = [ 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth' ]
				if passport_entry[ ECL ] not in eye_colors:
					result = False
					invalid_fields.append( ECL )

			if field == PID:
				pid = passport_entry[ PID ]
				if len( pid ) != 9 or type( int( pid ) ) != int:
					result = False
					invalid_fields.append( PID )

	return result, missing_fields, invalid_fields



if __name__ == "__main__":
	# input = r'D:\Projects\Python\Personal\Advent_of_Code\2020\day_04_input.txt'
	input = r'D:\Dropbox\Projects\Python\Advent_of_Code\2020\day_04_input.txt'

	passport_db = [ ]
	data_dict = { }

	with open( input, 'r' ) as input_file:
		data = input_file.read( ).split( '\n\n' )

	expanded_check = True
	# data = test_data
	for line_num, line in enumerate( data ):
		# print( line_num )
		# print( "{'" + line.replace( '\n', ' ' ).replace( ' ', "', '" ).replace( ":", "' : '" ).strip( ) + "'}" )
		new_attributes = ast.literal_eval( "{'" + line.strip( ).replace( '\n', ' ' ).replace( ' ', "', '" ).replace( ":", "' : '" ) + "'}" )
		data_dict.update( new_attributes )

		cid = 'None'
		if 'cid' in data_dict.keys( ):
			cid = data_dict[ 'cid' ]

		result, missing_fields, invalid_fields = verify_data( data_dict, expanded_check = expanded_check )

		if result:
			new_entry = Passport_Entry( data_dict[ 'byr' ],
		                               data_dict[ 'iyr' ],
		                               data_dict[ 'eyr' ],
		                               data_dict[ 'hgt' ],
		                               data_dict[ 'hcl' ],
		                               data_dict[ 'ecl' ],
		                               data_dict[ 'pid' ],
		                               cid = cid )
			passport_db.append( new_entry )

		else:
			if expanded_check:
				print( '[ {0} ] Missing fields: {1}\t\tInvalid Fields: {2}'.format( line_num + 1, missing_fields, invalid_fields ) )
			else:
				print( '[ {0} ] Missing fields: {1}'.format( line_num + 1, missing_fields ) )

		data_dict = { }

	print( "\nValid number of entries: {0}".format( len( passport_db ) ) )