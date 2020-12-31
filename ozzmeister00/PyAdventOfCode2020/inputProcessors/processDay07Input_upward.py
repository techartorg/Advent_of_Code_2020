import collections
import random
import itertools

inputFile = r"D:\Advent_of_Code_2020\ozzmeister00\PyAdventOfCode2020\inputs\day07.txt"
testFile = r"D:\Advent_of_Code_2020\ozzmeister00\PyAdventOfCode2020\inputs\day07_test.txt"

inputFiles = [testFile, inputFile]

# format:
# MyRow,"(""Thing"",""OtherThing""),"(B=0,G=0,R=0,A=0)"

# make a list of possible colors to pick from

colors = []

values = list(range(0, 256))

colorValues = [i for i in itertools.product(values, repeat=3)]

for r, g, b in colorValues:
    color = '"(B={},G={},R={},A=255)"'.format(b, g, r)
    colors.append(color)


def main():
    for filePath in inputFiles:
        with open(filePath, 'r') as fh:
            lines = fh.readlines()

            outCSV = 'RowID,Parents,Color\n'
            for line in lines:
                bagID = line.split(' bags ', 1)[0].strip().replace(' ', '')
                containSplit = line.split(' contain ')[-1].strip()

                outCSV += bagID + ',"('

                if containSplit != 'no other bags.' and containSplit.strip():
                    contents = containSplit.split(',')

                    contentsDict = collections.defaultdict(int)

                    for content in contents:
                        content = content.lstrip()  # make sure to clear out trailing spaces
                        count = int(content.strip().split(' ')[0])

                        bag = content.split(' ', 1)[-1].replace('bags', '').replace('bag', '').replace('.', '').strip().replace(' ','')
                        contentsDict[bag] = count

                    bagStrings = []

                    for bag, count in contentsDict.items():
                        bagString = '(""{0}"", {1})'.format(bag, count)
                        bagStrings.append(bagString)

                    outCSV += ','.join(bagStrings)

                outCSV += ')",'

                # make sure we flag and hardcode the value for shinygold
                if bagID == 'shinygold':
                    color = '"(B=49,G=187,R=224,A=0)"'
                else:
                    # pop a color off the list so it can't be used again
                    color = colors.pop(random.randint(0, len(colors)))

                outCSV += color + '\n'

            with open(filePath.replace('.txt', '.csv'), 'w') as outFH:
                outFH.write(outCSV)

main()
