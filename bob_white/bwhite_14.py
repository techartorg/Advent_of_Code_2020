import re
from collections import defaultdict
from operator import setitem

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
        bin_val = "".join(a if b == "X" else b for a, b in zip(bin(int(val))[2:].rjust(36, "0"), mask))
        memory[int_addr] = int(bin_val, 2)
print(sum(memory.values()))

memory.clear()
mask = ""
for line in pzl:
    loc, val = line.split(" = ")
    if loc == "mask":
        mask = val
    elif loc.startswith("mem"):
        int_addr = int(regex.findall(loc)[0])
        bin_addr = bin(int_addr)[2:].rjust(36, "0")
        addrs = [list(bin_addr)]
        # Creating the collection of addresses from the mask is a little funny.
        # But we start with the unmasked address, then update each bit based on the mask, creating 2 new address for any X (with 0 and 1 values)
        for idx, v in enumerate(mask):
            if v == "1":
                addrs[:] = [addr[:] for addr in addrs if not setitem(addr, idx, "1")]
            elif v == "X":
                addrs[:] = [addr[:] for addr in addrs for nv in ("0", "1") if not setitem(addr, idx, nv)]
        for addr in addrs:
            memory[int("".join(addr), 2)] = int(val)
print(sum(memory.values()))