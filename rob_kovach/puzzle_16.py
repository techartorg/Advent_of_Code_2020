input_ = '''class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
'''

location = __file__
input_ = open(location.replace('.py', '_input.txt')).read()


rulesDict = {}
rules, myTicket, nearbyTickets = input_.split('\n\n')

myTicket = myTicket.split('your ticket:\n')[-1]
myTicket = [int(x) for x in myTicket.split(',')]
print(myTicket)


validRanges = []

rules = rules.splitlines()
for r in rules:
    field, values = r.split(': ', 1)
    values = values.split(' or ', 1)

    rulesDict[field] = []
    for v in values:

        min_, max_ = v.split('-')
        range_ = range(int(min_), int(max_)+1)
        rulesDict[field].append(range_)
        validRanges.append(range_)


nearbyTickets = nearbyTickets.splitlines()[1:]
nearbyTickets = [x.split(',') for x in nearbyTickets]
validTickets = []

tally = 0
for t in nearbyTickets:
    invalidTicket = False
    for number in t:
        n = int(number)

        invalid = True
        for r in validRanges:
            if n in r:
                invalid = False

        if invalid:
            invalidTicket = True
            tally += n
    if not invalidTicket:
        validTickets.append(t)

print(tally)


def get_values_of_fields(tickets):
    fieldsCount = len(tickets[0])
    ranges = [[] for _ in range(fieldsCount)]
    for i in range(fieldsCount):
        for t in tickets:
            ranges[i].append(int(t[i]))
    return ranges


def get_matching_fields(numbers):
    unmatchedFields = []
    matchedFields = []
    for field, ranges in rulesDict.items():
        valid = True
        for n in numbers:
            if n not in ranges[0] and n not in ranges[1]:
            #if n in ranges[0] or n in ranges[1]:
                unmatchedFields.append(field)
                valid = False
                break
        if valid:
            matchedFields.append(field)
    return list(set(matchedFields))


def eliminate_fields():
    count = 0
    locatedFields = {}
    fieldRanges = get_values_of_fields(validTickets)
    potentialFields = [get_matching_fields(r) for r in fieldRanges]
    numOfFields = len(rulesDict.keys())
    while count < numOfFields:
        for i, x in enumerate(potentialFields):
            if len(x) == 1:
                print(f'Field {x} is entry {i}.')
                # Store the field name and the column
                locatedFields[x[0]] = i
                count += 1

                # remove the located field from all other columns
                for j in range(len(potentialFields)):
                    potentialFields[j] = list(set(potentialFields[j]).difference(locatedFields.keys()))

    return locatedFields


def parse_my_ticket():
    value = 1
    fields = eliminate_fields()
    for field, index in fields.items():
        if field.startswith('departure'):
            value *= myTicket[index]
    return value


print(parse_my_ticket())