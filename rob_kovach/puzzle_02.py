"""
Advent of Code 2020 - Day 2: Password Philosophy

--- Part 1 ---
For example, suppose you have the following list:

    1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc


Each line gives the password policy and then the password. The password 
policy indicates the lowest and highest number of times a given letter 
must appear for the password to be valid. For example, 1-3 a means that 
the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, 
is not; it contains no instances of b, but needs at least 1. The first 
and third passwords are valid: they contain one a or nine c, both within 
the limits of their respective policies.

How many passwords are valid according to their policies?

--- Part 2 ---
While it appears you validated the passwords correctly, they don't seem 
to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the 
password policy rules from his old job at the sled rental place down the 
street! The Official Toboggan Corporate Policy actually works a little 
differently.

Each policy actually describes two positions in the password, where 1 means 
the first character, 2 means the second character, and so on. (Be careful; 
Toboggan Corporate Policies have no concept of "index zero"!) Exactly one 
of these positions must contain the given letter. Other occurrences of the 
letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.


How many passwords are valid according to the new interpretation of the policies?
"""

location = __file__
input_ = open(location.replace('.py', '_input.txt')).read()

def part1():
    passed = 0
    passwords = input_.splitlines()
    for item in passwords:
        policy, password = item.split(':')
        range_, requirement = policy.split(' ')
        min_, max_ = range_.split('-')
        count = password.count(requirement)
        if count >= int(min_) and count <= int(max_):
            passed += 1
    return passed

def part2():
    passed = 0
    passwords = input_.splitlines()
    for item in passwords:
        policy, password = item.split(':')
        password = password.strip()
        range_, requirement = policy.split(' ')
        min_, max_ = range_.split('-')
        match1 = password[int(min_)-1] == requirement
        match2 = password[int(max_)-1] == requirement
        if match1 != match2:
            passed +=1

    return passed


print(part1())
print(part2())