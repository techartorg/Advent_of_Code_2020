from typing import Dict, Callable, Tuple, List, Set


class Machine(object):
    ops: Dict[str, Callable[[int], None]]
    acc: int = 0

    pointer: int = 0
    visited: Set[int] = set()

    def __init__(self, ins: List[Tuple[str, int]]):
        self.ops = {
            "nop": self.op_nop,
            "acc": self.op_acc,
            "jmp": self.op_jmp,
        }
        self.ins = ins

    def op_nop(self, _: int):
        self.pointer += 1

    def op_acc(self, arg: int):
        self.acc += arg
        self.pointer += 1

    def op_jmp(self, arg: int):
        self.pointer += arg

    def __iter__(self):
        return self

    def __next__(self):
        if self.pointer in self.visited:
            raise ValueError("infinite loop detected in data")

        self.visited.add(self.pointer)

        if self.pointer >= len(self.ins):
            raise StopIteration()

        op, arg = self.ins[self.pointer]
        self.ops[op](arg)

        return self.acc

    def reset(self):
        self.pointer = 0
        self.acc = 0
        self.visited.clear()


with open("inputs/day08.txt", 'r') as f:
    instructions = ((*line.split(maxsplit=1),) for line in f.read().splitlines())
    instructions = [(op, int(arg)) for op, arg in instructions]
    machine = Machine(instructions)

    try:
        for _ in machine:
            pass
    except ValueError:
        print(f"part a: {machine.acc}")

    machine.reset()

    for i, op, arg in ((i, *ins) for i, ins in enumerate(machine.ins) if ins[0] in ("nop", "jmp")):
        new_op = "nop" if op == "jmp" else "jmp"

        machine.ins[i] = (new_op, arg)

        try:
            for _ in machine:
                pass
            print(f"part b: {machine.acc}")
            break
        except ValueError:
            machine.ins[i] = (op, arg)
            machine.reset()
