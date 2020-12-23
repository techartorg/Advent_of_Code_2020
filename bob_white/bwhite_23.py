# I really wanted to make this work with deques, but I couldn't wrap my head around it.
circle = list(map(int, open("day_23.input").read()))
# circle = list(map(int, "389125467"))

max_val = max(circle)
cir_len = len(circle)
current_cup = circle[0]
for _ in range(100):
    idx = circle.index(current_cup)
    move = []
    for _ in range(3):
        try:
            move.append(circle.pop(idx + 1))
        except IndexError:
            # If we can't grab it off the end, we yank it from the front.
            move.append(circle.pop(0))
    dest = current_cup - 1
    while dest not in circle:
        dest = max_val if dest == 0 else dest - 1
    insert = circle.index(dest)
    for i, v in enumerate(move, 1):
        circle.insert(insert + i, v)
    current_cup = circle[(circle.index(current_cup) + 1) % cir_len]
print("".join(list(map(str, (circle[circle.index(1) :] + circle[: circle.index(1)])[1:]))))


values = list(map(int, open("day_23.input").read()))
# values = list(map(int, "389125467"))

MAX = 1000000
MIN = 1
values.extend(range(max(values) + 1, MAX + 1))
# Using a dictionary as a poor mans linked list, every node points to the next node in values
# this turns out to be much smarter than the lists I used for part 1
# Same with using deque, even though its a linked list under the hood, lookup times are still O(N)
# Dict gets me O(1)
ring = {values[-1]: values[0]} | {a: b for a, b in zip(values, values[1:])}

current = values[0]
for x in range(MAX * 10):
    next_val = ring[current]
    # Capture the next 3 nodes in the ring
    move = [-1, -1, -1]
    for x in range(3):
        move[x] = next_val
        next_val = ring[next_val]
    # Close back over the hole.
    ring[current] = next_val
    dest = current - 1 or MAX
    while dest in move:
        dest = dest - 1 if dest > MIN else MAX
    # Insert them into their new location
    insert = ring[dest]
    ring[dest] = move[0]
    ring[move[2]] = insert
    current = next_val
print(ring[1] * ring[ring[1]])
