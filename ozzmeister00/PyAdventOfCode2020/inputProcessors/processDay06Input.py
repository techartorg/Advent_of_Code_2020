import string

inputFile = r"D:\Advent_of_Code_2020\ozzmeister00\PyAdventOfCode2020\inputs\day06.txt"
testFile = r"D:\Advent_of_Code_2020\ozzmeister00\PyAdventOfCode2020\inputs\day06_test.txt"

inputFiles = [inputFile, testFile]

def chunkify(inData, startIndex):
    """

    :param list inData: the list of individual answers, split by newline
    :param startIndex: where to start parsing from
    :return int, str: the index we ended at, and the generated chunk string
    """
    outValue = ''
    end = False
    index = startIndex

    while not end and index < len(inData):
        currentEntry = inData[index]
        if currentEntry == '\n':
            end = True
        else:
            outValue += currentEntry

        index += 1

    outValue = outValue.replace('\n', ' ')

    return index, outValue


def main():
    for filePath in inputFiles:
        with open(filePath, 'r') as fh:
            lines = fh.readlines()

            groups = []

            j = 0
            while j < len(lines):
                j, chunk = chunkify(lines, j)
                groups.append(chunk)

            groupAnswers = []

            for group in groups:
                group = sorted(list(set(group)))
                groupAnswers.append(['1' if letter in group else '0' for letter in string.ascii_lowercase])

            i = 0
            outCSV = 'RowID,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z\n'
            for groupAnswer in groupAnswers:
                outCSV += str(i) + ',' + ','.join(groupAnswer) + '\n'
                i += 1

            with open(filePath.replace('.txt', '.csv'), 'w') as outFH:
                outFH.write(outCSV)

main()
