"""
Advent of Code 2020 - Day 1: Report Repair

--- Part 1 ---
Before you leave, the Elves in accounting just need you to fix your expense 
report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and 
then multiply those two numbers together.

For example, suppose your expense report contained the following:
1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying 
them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that 
sum to 2020; what do you get if you multiply them together?

--- Part 2 ---
The Elves in accounting are thankful for your help; one of them even offers 
you a starfish coin they had left over from a past vacation. They offer you 
a second one if you can find three numbers in your expense report that meet 
the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 
366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that 
sum to 2020?

"""

location = __file__
input_ = open(location.replace('.py', '_input.txt')).read()

expenses = [int(x) for x in input_.splitlines()]

def part1():
    _sum = 2020
    for x in expenses:
        diff = _sum - x
        if diff in expenses:
            return x * diff

def part2():
    _sum = 2020
    for i, val in enumerate(expenses):
        for j in range(i+1, len(expenses)):
            diff = _sum - (val + expenses[j])
            if diff in expenses:
                return diff * val * expenses[j]

print(part1())
print(part2())
