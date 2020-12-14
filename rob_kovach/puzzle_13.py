"""
Advent of Code - Day 13
"""

location = __file__
input_ = open(location.replace('.py', '_input.txt')).read().splitlines()

TIME = int(input_[0])
part1_ids = [int(x) for x in input_[1].split(',') if x != 'x']
part2_ids = [x for x in input_[1].split(',')]

def get_closet_departure_time(busId):
    time = 0
    while time <= TIME:
        time += busId
    return time

def part1():
    departure_times = {}
    for id_ in part1_ids:
        departure_time = get_closet_departure_time(id_)
        departure_times[departure_time] = id_
    closest_time = min(departure_times.keys())
    return (closest_time - TIME) * departure_times[closest_time]


'''
# Brute Force Part 2 - Solves the sample data, but the puzzle data is too
# much for a brute force solve.

def part2():

    pattern_matched = False

    while not pattern_matched:
        matched = 0
        starting_bus = int(bus_ids2[0])
        for i in range(1, len(bus_ids2)):
            try:
                id_ = int(bus_ids2[i])
            except:
                continue
            
            if ((time_stamp + i) / int(id_)).is_integer():
                matched += 1
            else:
                break
        if (matched + 1) == len(bus_ids):
            pattern_matched = True
        else:
            matched = 0
        time_stamp += starting_bus
    return time_stamp - starting_bus
'''



def part2():
    """
    Had a lot of help with this one from my colleagues Jim Gage and Dan Higdon.
    Couldn't have done it without them!
    """
    time = 0
    delta = int(part2_ids[0])
    i = 1
    while i < len(part2_ids):
        try:
            busId = int(part2_ids[i])
        except:
            i += 1
        else:
            if ((time + i) % busId) == 0:
                delta *= busId
                i += 1
            else:
                time += delta
    return time


if __name__ == '__main__':
    print(part1())
    print(part2())