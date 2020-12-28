# CSV format:
# byr, iyr, eyr, hgt, hcl, ecl, pid, cid
# BirthYear, IssueYear, ExpirationYear, Height, HairColor, EyeColor, PassportID, CountryID

inputFile = r"D:\Advent_of_Code_2020\ozzmeister00\PyAdventOfCode2020\inputs\day04.txt"
testFile = r"D:\Advent_of_Code_2020\ozzmeister00\PyAdventOfCode2020\inputs\day04_test.txt"
testFilePart02 = r"D:\Advent_of_Code_2020\ozzmeister00\PyAdventOfCode2020\inputs\day04_part2_test.txt"

inputFiles = [testFilePart02]

class Entry(object):
    def __init__(self, inString):
        data = inString.split(' ')

        dataDict = {'byr':'',
                    'iyr':'',
                    'eyr':'',
                    'hgt':'',
                    'hcl':'',
                    'ecl':'',
                    'pid':'',
                    'cid':''}

        for item in data:
            if item:
                key, value = item.split(':')
                dataDict[key] = value

        self.birthYear = dataDict['byr']
        self.issueYear = dataDict['iyr']
        self.expirationYear = dataDict['eyr']
        self.height = dataDict['hgt']
        self.hairColor = dataDict['hcl']
        self.eyeColor = dataDict['ecl']
        self.passportID = dataDict['pid']
        self.countryID = dataDict['cid']

    def isValid(self):
        """

        :return bool:
        """
        return self.birthYear and self.issueYear and self.expirationYear and self.height and self.hairColor and self.eyeColor and self.passportID

    def toCSV(self):
        """
        Convert the Entry object into a line for a CSV file

        :return str: the entry converted to a CSV
        """
        outString = ''
        outString += self.birthYear
        outString += ','
        outString += self.issueYear
        outString += ','
        outString += self.expirationYear
        outString += ','
        outString += self.height
        outString += ','
        outString += self.hairColor
        outString += ','
        outString += self.eyeColor
        outString += ','
        outString += self.passportID
        outString += ','
        outString += self.countryID

        return outString


def chunkifyDB(inDB, startIndex):
    """

    :param list inDB: the list of database entries, split by newline
    :param startIndex: where to start parsing from
    :return int, str: the index we ended at, and the generated chunk string
    """
    outValue = ''
    end = False
    index = startIndex

    while not end and index < len(inDB):
        currentEntry = inDB[index]
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
            chunks = []
            i = 0
            while i < len(lines):
                i, chunk = chunkifyDB(lines, i)
                chunks.append(chunk)

            outCSV = 'RowID,BirthYear,IssueYear,ExpirationYear,Height,HairColor,EyeColor,PassportID,CountryID\n'
            counter = 0
            for i, chunk in enumerate(chunks):
                entry = Entry(chunk)
                if entry.isValid():
                    counter += 1
                else:
                    print(i)

                outCSV += str(i) + ',' + entry.toCSV() + '\n'

            with open(filePath.replace('.txt','.csv'), 'w') as outFH:
                outFH.write(outCSV)

            #print(counter)

main()