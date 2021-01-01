inputFile = r"D:\Advent_of_Code_2020\ozzmeister00\PyAdventOfCode2020\inputs\day08.txt"
testFile = r"D:\Advent_of_Code_2020\ozzmeister00\PyAdventOfCode2020\inputs\day08_test.txt"

inputFiles = [testFile, inputFile]

enumTranslator = {'acc': "Accumulate",
                  'jmp': "Jump",
                  'nop': "NoOperation"
                  }


def main():
    for filePath in inputFiles:
        with open(filePath, 'r') as fh:
            lines = fh.readlines()

            outCSV = 'RowID,Operator,Value\n'
            for i, line in enumerate(lines):
                operator, value = line.split(' ')
                operator = enumTranslator[operator]
                value = int(value)  # convert the in string
                outCSV += str(i) + ',"{}"'.format(operator) + ',"{}"'.format(value) + '\n'

            with open(filePath.replace('.txt', '.csv'), 'w') as outFH:
                outFH.write(outCSV)

main()
