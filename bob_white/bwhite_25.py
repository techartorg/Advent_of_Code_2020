door, card = map(int, open("day_25.input").read().splitlines())

loop_size = 1
subject_number = 7
found = 0
door_loop = 0
card_loop = 0
while found != 2:
    loop_size += 1
    subject_number *= 7
    subject_number %= 20201227
    if subject_number == door:
        door_loop = loop_size
        found += 1
    if subject_number == card:
        card_loop = loop_size
        found += 1

door_key = 1
for _ in range(card_loop):
    door_key *= door
    door_key %= 20201227
print(door_key)
card_key = 1
for _ in range(door_loop):
    card_key *= card
    card_key %= 20201227
print(card_key)
