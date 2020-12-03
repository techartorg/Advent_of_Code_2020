'''
We're going to output this data as a csv with id, value so we can import it into Unreal as a float curve
'''
import os

inputFile = 'D:\Advent_of_Code_2020\ozzmeister00\PyAdventOfCode2020\inputs\day01.txt'
outputFile = 'D:\Advent_of_Code_2020\ozzmeister00\PyAdventOfCode2020\inputs\day01.csv'

with open(inputFile, 'r') as fh:
    data = fh.read()
    lines = data.split('\n')

    outData = ''

    for i, line in enumerate(lines):
        outData += str(i) + ',' + line + '\n'

    with open(outputFile, 'w') as fh:
        fh.write(outData)
