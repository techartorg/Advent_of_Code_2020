"""

"""

from lib.helpers import timer
input_nums = open("inputs/day15_input.txt", "r").read().split(',')


@timer
def solution(inputs, ending_number):
    num_list = {int(num): ind + 1 for ind, num in enumerate(inputs)}
    itr = len(inputs)
    current_num = int(inputs[-1])
    while itr < ending_number:
        if current_num not in num_list:
            num_list[current_num] = itr
            current_num = 0
        else:
            last_num = current_num
            current_num = itr - num_list[last_num]
            num_list[last_num] = itr
        itr += 1
    return current_num


print(solution(input_nums, 2020))
print(solution(input_nums, 30000000))
