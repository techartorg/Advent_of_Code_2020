"""
Advent of Code - Day 8
"""

location = __file__
input_ = open(location.replace('.py', '_input.txt')).read().splitlines()

def part1(dataset):
    """
    Execute the actions and record their index until the current action
    would execute an action already in the list of recoded indices.
    Break and return the accumulation value.
    """

    bootSuccessful = True
    accumulation = 0

    recordedActions = []
    i = 0 
    while i < len(dataset):
        recordedActions.append(i)
        action = dataset[i]
        value = int(action.split(' ', 1)[-1])
        if 'acc' in action:
            accumulation += value
            i += 1
        elif 'jmp' in action:
            i += value
        elif 'nop' in action:
            i += 1
        if i in recordedActions:
            bootSuccessful = False
            break
    return bootSuccessful, accumulation

def part2(dataset):
    """
    For each "jmp" and "nop" action in the action list, try swapping
    the action and booting the sequence. If we successfully boot, break
    and return the accumulation value.
    """
    for i, action in enumerate(dataset):
        datacopy = list(dataset)
        value = int(action.split(' ')[-1])
        if value == 0:
            continue
        if 'jmp' in action:
            new_action = action.replace('jmp', 'nop')
            datacopy[i] = new_action
        elif 'nop' in action:
            new_action = action.replace('nop', 'jmp')
            datacopy[i] = new_action
        else:
            continue
        result, accumulation = part1(datacopy)
        if result:
            return accumulation
    
if __name__ == '__main__':
    print(part1(input_)[1])
    print(part2(input_))