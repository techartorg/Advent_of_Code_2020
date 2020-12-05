"""
Advent of Code - Day 5
"""

test_input = '''FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
'''

location = __file__
boarding_passes = open(location.replace('.py', '_input.txt')).read().splitlines()

def parse_boarding_pass(boardingpass):
    rows = 128
    columns = 8
    
    def get_row():
        divisor = 0.5
        row = [0, 127]
        for i in boardingpass[:6]:
            offset = rows * divisor
            if i == 'F':
                row[1] -= offset
            elif i == 'B':
               row[0] += offset
            divisor *= 0.5
        if boardingpass[6] == 'F':
            return int(min(row))
        else:
            return int(max(row))
    
    def get_column():
        divisor = 0.5
        column = [0, 7]
        for i in boardingpass[7:9]:
            offset = columns * divisor
            if i == 'L':
                column[1] -= offset
            elif i == 'R':
                column[0] += offset
            divisor *= 0.5
        if boardingpass[9] == 'L':
            return int(min(column))
        else:
            return int(max(column))
    
    return get_row() * 8 + get_column()

def part1():
    max_seat_id = 0
    for boarding_pass in boarding_passes:
        seat_id = parse_boarding_pass(boarding_pass)
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    return max_seat_id

def part2():
    seat_ids = [parse_boarding_pass(x) for x in boarding_passes]
    all_seats = range(min(seat_ids), max(seat_ids))
    missing_seats = list(set(all_seats).difference(seat_ids))
    return missing_seats

if __name__ == '__main__':
    print(part1())
    print(part2())
