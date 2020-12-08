"""
--- Day 5: Binary Boarding ---
You board your plane only to discover a new problem: you dropped your boarding pass! You aren't sure which seat is yours, and all of the flight attendants are busy with the flood of people that suddenly made it through passport control.
You write a quick program to use your phone's camera to scan all of the nearby boarding passes (your puzzle input); perhaps you can find your seat through process of elimination.

Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".
The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.
[...]
Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.
As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?

--- Part Two ---

It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.
Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?
"""

def find_position(seat_lines, code):
	if len(seat_lines)==1:
		return(seat_lines[0])
	else:
		k=code[0]
		new_code = code[1:]
		if k in ('F','L'):
			return find_position(seat_lines[0:len(seat_lines)//2], new_code)
		elif k in ('B','R'):
			return find_position(seat_lines[len(seat_lines)//2:], new_code)

codes = [d for d in open('./input_05.txt', 'r').read().split()]
ids = sorted([find_position(list(range(0,128)),code[:7]) * 8 + find_position(list(range(0,8)),code[7:]) for code in codes])
print(f"The highest seat ID on a boarding pass is: {ids[-1]}")
print(f"Your seat id is: {list(set(range(ids[0], ids[-1]+1))-set(ids))[0]}")
