# I really wanted to make this work with deques, but I couldn't wrap my head around it.
# For part 2 I came up with the bright idea of using a dict to act as a linked list, or at least a circular mapping structure
# Back ported that to part 1 because I liked it more.
values = list(map(int, open("day_23.input").read()))
# circle = list(map(int, "389125467"))
ring = {a: b for a, b in zip(values, values[1:] + [values[0]])}

MAX = max(values)
MIN = 1

current = values[0]
for _ in range(100):
    next_val = ring[current]
    move = [-1, -1, -1]
    for x in range(3):
        move[x] = next_val
        next_val = ring[next_val]
    ring[current] = next_val

    dest = current - 1 or MAX
    while dest in move:
        dest = dest - 1 if dest > MIN else MAX

    insert = ring[dest]
    ring[dest] = move[0]
    ring[move[2]] = insert
    current = next_val

ring_vals = []
x = 1
while (x := ring[x]) != 1:
    ring_vals.append(x)
print("".join(map(str, ring_vals)))


values = list(map(int, open("day_23.input").read()))
# values = list(map(int, "389125467"))

MAX = 1000000
values.extend(range(max(values) + 1, MAX + 1))
# Using a dictionary as a poor mans linked list, every node points to the next node in values
# this turns out to be much smarter than the lists I used for part 1
# Same with using deque, even though its a linked list under the hood, lookup times are still O(N)
# Dict gets me O(1)
ring = {a: b for a, b in zip(values, values[1:] + [values[0]])}
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
