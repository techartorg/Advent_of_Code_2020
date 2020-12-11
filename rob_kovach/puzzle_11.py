"""
Advent of Code - Day 11
"""

location = __file__
input_ = open(location.replace('.py', '_input.txt')).read().splitlines()

columns = len(input_[0])
rows = len(input_)

seating_array = []
for line in input_:
    seating_array.append(list(line))

OCCUPIED = '#'
SEAT = 'L'
FLOOR = '.'


def is_seat(row, column, seatingChart):
    seat = seatingChart[row][column]
    return seat == SEAT or seat == OCCUPIED


def is_seat_occupied(row, column, seatingChart):
    seat = seatingChart[row][column]
    return seat == OCCUPIED


def get_neighbor(row, column, offsetX, offsetY, seatingChart):
    if row + offsetY in range(rows) and column + offsetX in range(columns):
        return seatingChart[row + offsetY][column + offsetX]
    return None


def occupied_neighbors(row, column, seatingChart):
    neighbors = [[-1, -1], [-1, 0], [-1, 1],
                 [0, -1], [0, 1],
                 [1, -1], [1, 0], [1, 1]]
    if seatingChart[row][column] == FLOOR:
        return None
    count = 0
    for x, y in neighbors:
        neighbor = get_neighbor(row, column, x, y, seatingChart)
        if neighbor:
            if neighbor == OCCUPIED:
                count +=1
    return count


def is_seat_available(row, column, seatingChart):
    return occupied_neighbors(row, column, seatingChart) == 0


def is_time_to_go(row, column, seatingChart):
    return occupied_neighbors(row, column, seatingChart) >= 4


def musical_chairs():
    previous_round = seating_array
    current_round = [sublist[:] for sublist in previous_round]
    occupied_seats = 0
    while True:
        for row in range(rows):
            for col in range(columns):
                if is_seat(row, col, previous_round):
                    if not is_seat_occupied(row, col, previous_round):
                        if is_seat_available(row, col, previous_round):
                            occupied_seats += 1
                            current_round[row][col] = OCCUPIED
                    else:
                        if is_time_to_go(row, col, previous_round):
                            occupied_seats -= 1
                            current_round[row][col] = SEAT

        if current_round == previous_round:
            break
        else:
            previous_round = [sublist[:] for sublist in current_round]
    return occupied_seats

print(musical_chairs())


# Part 2 ------------------------------------------------------------------------------
def find_neighbors_along_direction(row, column, offsetX, offsetY, seatingChart):
    x = offsetX
    y = offsetY
    while True:
        neigh = get_neighbor(row, column, x, y, seatingChart)
        if not neigh:
            return 0
        else:
            if neigh == OCCUPIED:
                return 1
            elif neigh == SEAT:
                return 0
        x += offsetX
        y += offsetY


def occupied_neighbors2(row, column, seatingChart):
    neighbors = [[-1, -1], [-1, 0], [-1, 1],
                 [0, -1], [0, 1],
                 [1, -1], [1, 0], [1, 1]]
    count = 0
    for x, y in neighbors:
        count += find_neighbors_along_direction(row, column, x, y, seatingChart)
    return count


def is_seat_available2(row, column, seatingChart):
    return occupied_neighbors2(row, column, seatingChart) == 0


def is_time_to_go2(row, column, seatingChart):
    return occupied_neighbors2(row, column, seatingChart) >= 5


def musical_chairs2():
    previous_round = seating_array
    current_round = [sublist[:] for sublist in previous_round]
    occupied_seats = 0
    while True:
        for row in range(rows):
            for col in range(columns):
                if is_seat(row, col, previous_round):
                    if not is_seat_occupied(row, col, previous_round):
                        if is_seat_available2(row, col, previous_round):
                            occupied_seats += 1
                            current_round[row][col] = OCCUPIED
                    else:
                        if is_time_to_go2(row, col, previous_round):
                            occupied_seats -= 1
                            current_round[row][col] = SEAT

        if current_round == previous_round:
            break
        else:
            previous_round = [sublist[:] for sublist in current_round]
    return occupied_seats


print(musical_chairs2())