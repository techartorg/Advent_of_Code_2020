from functools import reduce
import itertools
import operator


all_input = open('day1_input.txt').readlines()
for i in range(2, 4):
    for values in itertools.combinations(all_input, i):
        if sum(map(int, values)) == 2020:
            print(reduce(operator.mul, map(int, values)))
            break
