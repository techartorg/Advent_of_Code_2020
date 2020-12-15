import re
import time
from itertools import product


def replace_at_index(collection, index, value):
    col = collection[:]
    col[index] = value
    return col


pzl = open("day_14.input").read().splitlines()

regex = re.compile(r"\[(\d+?)\]")
part_01 = {}
part_02 = {}
mask = ""
mask_map = {}

for line in pzl:
    loc, val = line.split(" = ")
    if loc == "mask":
        mask = val
        mask_map = {idx: ["1"] if v == "1" else ["0", "1"] for idx, v in enumerate(val) if v != "0"}
    elif loc.startswith("mem"):
        bin_address = f"{int(regex.findall(loc)[0]):036b}"
        masked_val = "".join(val_bit if mask_bit == "X" else mask_bit for val_bit, mask_bit in zip(f"{int(val):036b}", mask))
        part_01[bin_address] = int(masked_val, 2)

        # Creating the collection of addresses from the mask is a little funny.
        # But we start with the unmasked address, then update each bit based on the mask, creating 2 new address for any X (with 0 and 1 values)
        masked_addresses = [list(bin_address)]
        for idx, new_vals in mask_map.items():
            masked_addresses[:] = [replace_at_index(address, idx, nv) for address in masked_addresses for nv in new_vals]
        assert len(masked_addresses) == 2 ** mask.count("X")  # We make a lot of masked_addresses.

        # This is about 10x faster. Less slicing less function calls, less iterations.
        masked_address = "".join(address_bit if mask_bit == "0" else "1" if mask_bit == "1" else "{}" for address_bit, mask_bit in zip(bin_address, mask))
        masked_address_strings = (masked_address.format(*p) for p in product([0, 1], repeat=mask.count("X")))

        for address in masked_address_strings:
            part_02[address] = int(val)

print(f"Part_01: {sum(part_01.values())}")
print(f"Part_02: {sum(part_02.values())}")
