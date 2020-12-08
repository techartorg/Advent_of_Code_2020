inputs = [(op, int(v)) for line in open("day_08.input").read().splitlines() for (op, v) in (line.split(),)]


def run_input(inputs):
    acc = 0
    inst = 0
    visited_instructions = set()
    while inst not in visited_instructions:
        try:
            op, v = inputs[inst]
        except IndexError:
            print(f"Part 02 {acc}")
            return None
        if op == "acc":
            acc += v
        elif op == "jmp":
            inst += v
            continue
        visited_instructions.add(inst)
        inst += 1

    return acc


print(f"Part 01: {run_input(inputs[:])}")
# Just brute force part 2. It is more than fast enough.
jmps = [(idx, op, v) for idx, (op, v) in enumerate(inputs) if op in ("jmp", "nop")]
for idx, op, v in jmps:
    n_inputs = inputs[:]
    n_inputs[idx] = ("nop" if op == "jmp" else "jmp", v)
    if run_input(n_inputs[:]) is None:
        break
