"""
--- Day 2: Password Philosophy ---
[...]

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?

--- Part Two ---
[...]
Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?
"""


from collections import Counter
import re

def count_valid_password_p1():
	with open('./input_02.txt', 'r') as f:
	    input_lines = f.read().split("\n")
	    valid = 0
	    for line in input_lines:
	    	if line!="":
		        min_occ, max_occ, char, password = re.split("-|: | ", line)
		        if Counter(password)[char] in range(int(min_occ), int(max_occ)+1):
		            valid += 1
	f.close()
	return(valid)

def count_valid_password_p2():
	with open('./input_02.txt', 'r') as f:
	    input_lines = f.read().split("\n")
	    valid = 0
	    for line in input_lines:
	    	if line!="":
		        pos1, pos2, char, password = re.split("-|: | ", line)
		        if (bool(password[int(pos1)-1]==char) ^ bool(password[int(pos2)-1]==char)):
		            valid += 1
	f.close()
	return(valid)

print(f"Valid passwords (part 1): {count_valid_password_p1()}")
print(f"Valid passwords (part 2): {count_valid_password_p2()}")