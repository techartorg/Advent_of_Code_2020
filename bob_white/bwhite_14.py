import re
from collections import defaultdict


def replace_at_index(collection, index, value):
    col = collection[:]
    col[index] = value
    return col


pzl = open("day_14.input").read().splitlines()

regex = re.compile(r"\[(\d+?)\]")
memory = defaultdict(int)
mask = ""
for line in pzl:
    loc, val = line.split(" = ")
    if loc == "mask":
        mask = val
    elif loc.startswith("mem"):
        int_addr = int(regex.findall(loc)[0])
        bin_val = "".join(a if b == "X" else b for a, b in zip(f"{int(val):036b}", mask))
        memory[int_addr] = int(bin_val, 2)
print(sum(memory.values()))

memory.clear()
mask_map = {}
for line in pzl:
    loc, val = line.split(" = ")
    if loc == "mask":
        mask_map = {idx: ["1"] if v == "1" else ["0", "1"] for idx, v in enumerate(val) if v != "0"}
    elif loc.startswith("mem"):
        int_addr = int(regex.findall(loc)[0])
        bin_addr = f"{int(int_addr):036b}"
        # Creating the collection of addresses from the mask is a little funny.
        # But we start with the unmasked address, then update each bit based on the mask, creating 2 new address for any X (with 0 and 1 values)
        addrs = [list(bin_addr)]
        for idx, new_vals in mask_map.items():
            addrs[:] = [replace_at_index(addr, idx, nv) for addr in addrs for nv in new_vals]
        for addr in addrs:
            memory[int("".join(addr), 2)] = int(val)
print(sum(memory.values()))
