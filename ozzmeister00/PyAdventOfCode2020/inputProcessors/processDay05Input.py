inputFile = r"D:\Advent_of_Code_2020\ozzmeister00\PyAdventOfCode2020\inputs\day05.txt"
testFile = r"D:\Advent_of_Code_2020\ozzmeister00\PyAdventOfCode2020\inputs\day05_test.txt"


inputFiles = [inputFile, testFile]

def isTrue(a):
    if a == 'B' or a == 'R':
        return 'true'
    return 'false'

def main():
    for filePath in inputFiles:
        with open(filePath, 'r') as fh:
            lines = fh.readlines()
            seatIDs = []

            for line in lines:
                seatIDs.append([isTrue(letter) for letter in list(line.strip())])

            outCSV = 'RowID,R64,R32,R16,R8,R4,R2,R1,S4,S2,S1\n'

            i = 0

            for seat in seatIDs:
                outCSV += str(i) + ',' + ','.join(seat) + '\n'
                i += 1

            with open(filePath.replace('.txt', '.csv'), 'w') as outFH:
                outFH.write(outCSV)

main()