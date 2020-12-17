import re


pattern = re.compile(
    r'(\d+)-(\d+) (\w): (\w+)'
)


all_input = open('day2_input.txt').readlines()
matches = [match.groups() for match in map(pattern.match, all_input)]


p1_valid_count = 0
p2_valid_count = 0
for mn, mx, char, pw in matches:
    char_count = pw.count(char)
    p1_valid_count += int(
        int(mn) <= char_count <= int(mx)
    )
    p2_valid_count += int(
        sum(
            (pw[int(mn)-1] == char,
             pw[int(mx)-1] == char)
        ) == 1
    )

print(p1_valid_count)
print(p2_valid_count)
