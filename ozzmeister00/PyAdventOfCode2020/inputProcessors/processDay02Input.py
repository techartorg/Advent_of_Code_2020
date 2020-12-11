inFile = r'D:\Advent_of_Code_2020\ozzmeister00\PyAdventOfCode2020\inputs\day02.txt'
outFile = r'D:\Advent_of_Code_2020\ozzmeister00\PyAdventOfCode2020\inputs\day02.csv'

with open(inFile, 'r') as fh:
    output = 'ID,Min,Max,Letter,Password\n'
    lines = fh.read().split('\n')

    i = 0

    for line in lines:
        policy, password = line.split(':')
        minMax, letter = policy.split(' ')
        minCount, maxCount = minMax.split('-')

        output += ','.join([str(i), minCount, maxCount, letter, password.strip()]) + '\n'

        i += 1

    with open(outFile, 'w') as fh:
        fh.write(output)
