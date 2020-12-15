"""

"""

import re
from itertools import product
from lib.helpers import timer

open_input = [(line.split(' = ')[0], line.split(' = ')[1]) for line in open("inputs/day14_input.txt", "r").read().splitlines()]
mem_pattern = re.compile(r'mem\[(.*?)\]')


@timer
def part01(input_list):
    current_mask = ''
    memory = {}
    for ind, (operation, value) in enumerate(input_list):
        if operation == 'mask':
            current_mask = value
        else:
            address = int(mem_pattern.match(operation).group(1))
            value = '{:036b}'.format(int(value))

            write_bin = ['0']*36
            for ind1, (val, mask) in enumerate(zip(value, current_mask)):
                if mask == 'X':
                    write_bin[ind1] = value[ind1]
                elif mask == '1':
                    write_bin[ind1] = '1'
                else:
                    write_bin[ind1] = '0'
            memory[address] = int(''.join(write_bin), 2)

    return sum(memory.values())


@timer
def part02(input_list):
    current_mask = ''
    memory = {}
    for operation, value in input_list:
        if operation == 'mask':
            current_mask = value
        else:
            address = '{:036b}'.format(int(mem_pattern.match(operation).group(1)))
            write_addr = ['0']*36
            for ind1, (val, mask) in enumerate(zip(address, current_mask)):
                if mask == '0':
                    write_addr[ind1] = val
                elif mask == '1':
                    write_addr[ind1] = '1'
                else:
                    write_addr[ind1] = '{}'
            perms = [tuple(prod) for prod in product(('0', '1'), repeat=write_addr.count('{}'))]
            for perm in perms:
                new_addr = ''.join(write_addr).format(*perm)
                memory[new_addr] = int(value)

    return sum(memory.values())


print(part01(open_input))
print(part02(open_input))
