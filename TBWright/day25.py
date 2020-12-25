"""

"""

f = open("inputs/day25_input.txt", "r")
card_key = int(f.readline().strip())
door_key = int(f.readline().strip())


def find_loop_size(key_val):
    val = 1
    loop = 0
    while val != key_val:
        loop += 1
        val = (val * 7) % 20_201_227
    return loop


def find_encryption_key(loop_num, sub_num):
    itr = 0
    val = 1
    while itr < loop_num:
        itr += 1
        val = (val * sub_num) % 20_201_227
    return val



card_loop_size = find_loop_size(card_key)

print(find_encryption_key(card_loop_size, door_key))