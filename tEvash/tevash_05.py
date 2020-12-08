with open("inputs_5.txt") as f:
	inputs = f.readlines()

ex_inputs = [
	"FBFBBFFRLR",
	"BFFFBBFRRR",
	"FFFBBBFRRR",
	"BBFFBBFRLL"
]

def part1(inputs):
	max_seat_id = -1
	seat_ids = []
	for b_pass in inputs:
		row_data = b_pass[:7]
		seat_data = b_pass[7:]
		rows = range(128)
		seats = range(8)
		for r in row_data:
			if r == "B":
				rows = rows[len(rows) //2:]
			elif r == "F":
				rows = rows[:len(rows) // 2]
			# print(rows)
		for s in seat_data:
			if s == "R":
				seats = seats[len(seats) // 2:]
			elif s == "L":
				seats = seats[: len(seats) // 2]
		
		# print(f"Row: {rows[0]}, Seat: {seats[0]}")
		max_seat_id = max_seat_id if max_seat_id > ((rows[0] * 8) + seats[0]) else ((rows[0] * 8) + seats[0])
		seat_ids.append((rows[0] * 8) + seats[0])
	print(f"Highest seat id : {max_seat_id}")
	return seat_ids

def part2(inputs):
	ids = sorted(part1(inputs))
	for index, seat in enumerate(ids):
		if seat + 1 != ids[index+1]:
			print(f"my id is {seat +1}")
			return

part1(inputs)
part2(inputs)

