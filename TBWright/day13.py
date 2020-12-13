"""

"""

from functools import reduce

open_input = open("inputs/day13_input.txt", "r")
earliest_timestamp = int(open_input.readline().strip())
bus_ids = [_id for _id in open_input.readline().strip().split(',')]

"""
Part 2 uses the Chinese Remainder Theorem. I can't even pretend to know what it fully does.
In short:
We are trying to solve `(time + ind) % _id == 0` for every bus in the list.
Find the first number that solves this for the first two buses, then find the least common multiple of those.
Then use that LCM as the new time, and solve for that and the third bus.
Continue doing this until we end up with a single value that satisfies all the buses.

https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
"""


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def chinese_remainder(n, a):
    _sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        _sum += a_i * mul_inv(p, n_i) * p
    return _sum % prod


def part01(bus_id_list, timestamp):
    _id, prop = 0, 0
    for bus_id in bus_id_list:
        if bus_id == 'x':
            continue
        n_prop = timestamp / int(bus_id)
        if n_prop % 1 > prop % 1:
            _id, prop = int(bus_id), n_prop
    return _id, prop, (_id * (round(prop)*_id - timestamp))


def part02(bus_id_list):
    a, n = [], []
    for ind, bus_id in enumerate(bus_id_list):
        if bus_id == 'x':
            continue
        a.append(int(bus_id) - ind % int(bus_id))
        n.append(int(bus_id))

    return chinese_remainder(n, a)


print(part01(bus_ids, earliest_timestamp))
print(part02(bus_ids))