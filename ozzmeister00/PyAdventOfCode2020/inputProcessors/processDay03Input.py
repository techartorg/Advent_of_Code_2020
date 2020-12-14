
inputFile = r"E:\Advent_of_Code_2020\ozzmeister00\PyAdventOfCode2020\inputs\day03.txt"
outputFile = r"E:\Advent_of_Code_2020\ozzmeister00\PyAdventOfCode2020\inputs\day03.csv"

with open(inputFile, 'r') as fh:
    out = 'id,TreeData\n'
    lines = fh.read().split('\n')

    for j, line in enumerate(lines):
        out += str(j) + ',"(' + line.replace('.', 'false,').replace('#','true,')[:-1] + ')"\n'

    with open(outputFile, 'w') as outFile:
        outFile.write(out)



