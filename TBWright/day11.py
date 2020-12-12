"""

"""

from time import perf_counter
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        ret = func(*args, **kwargs)
        print(f"{func.__name__.replace('_', ' ')} took: {perf_counter() - start:.8f} seconds")
        return ret
    return wrapper


inputs = {(x, y): state for y, line in enumerate(open("inputs/day11_input.txt", "r").read().splitlines()) for x, state in enumerate(line)}

EMPTY = 'L'
FLOOR = '.'
OCCUPIED = '#'

vector_range = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def get_occupied_cells(row, column, input_dict, skip_empty=False):
    itr = 0
    for x_vec, y_vec in vector_range:
        new_x, new_y = row+x_vec, column+y_vec
        while skip_empty and input_dict.get((new_x, new_y), EMPTY) not in [EMPTY, OCCUPIED]:
            new_x += x_vec
            new_y += y_vec
        itr += input_dict.get((new_x, new_y), EMPTY) == OCCUPIED

    return itr


@timer
def fill_seats(input_dict, occupied_threshold=4, skip_empty=False):
    loops = 0
    while True:
        buffer_dict = input_dict.copy()
        for (row, column), state in input_dict.items():
            occupied_cells = get_occupied_cells(row, column, input_dict, skip_empty=skip_empty)
            if state == EMPTY and occupied_cells == 0:
                buffer_dict[(row, column)] = OCCUPIED
            if state == OCCUPIED and occupied_cells >= occupied_threshold:
                buffer_dict[(row, column)] = EMPTY

        loops += 1

        if input_dict == buffer_dict:
            break
        input_dict = buffer_dict

    return list(input_dict.values()).count(OCCUPIED), loops


print(fill_seats(inputs))
print(fill_seats(inputs, occupied_threshold=5, skip_empty=True))
