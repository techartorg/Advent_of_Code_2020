from typing import Dict, Callable, Tuple, List


def machine(ins: List[Tuple[str, int]]):
    pointer = 0
    acc = 0
    visited = set()

    def op_nop(_: int):
        nonlocal pointer
        pointer += 1

    def op_acc(x: int):
        nonlocal acc, pointer
        acc += x
        pointer += 1

    def op_jmp(x: int):
        nonlocal pointer
        pointer += x

    ops: Dict[str, Callable[[int], None]] = {
        "nop": op_nop,
        "acc": op_acc,
        "jmp": op_jmp,
    }

    while pointer < len(ins):
        if pointer in visited:
            raise ValueError("infinite loop detected")
        visited.add(pointer)

        op, arg = ins[pointer]
        ops[op](arg)
        yield acc


with open("inputs/day08.txt", 'r') as f:
    instructions = ((*line.split(maxsplit=1),) for line in f.read().splitlines())
    instructions = [(op, int(arg)) for op, arg in instructions]

    try:
        acc = 0
        for i in machine(instructions[:]):
            acc = i
    except ValueError:
        print(f"part a: {acc}")

        for i, op, arg in ((i, *ins) for i, ins in enumerate(instructions) if ins[0] in ("nop", "jmp")):
            new_op = "nop" if op == "jmp" else "jmp"

            new_instructions = instructions[:]
            new_instructions[i] = (new_op, arg)

            acc = 0
            try:
                for a in machine(new_instructions):
                    acc = a
                print(f"part b: {acc}")
            except ValueError:
                pass
