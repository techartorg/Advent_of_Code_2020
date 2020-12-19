import re
from typing import Any

rules, messages = open("day_19.input").read().split("\n\n")
tree: dict[int, list[list[Any]]] = {
    int(k): [[int(v) if '"' not in v else v[1] for v in sub_rule.split()] for sub_rule in rule.split(" | ")] for line in rules.splitlines() for k, rule in (line.split(": "),)
}


def match(message, stack):
    # If there is no stack left, we're done.
    # Also part 2, if the stack has grown larger than the message, we're done.
    if not stack or len(stack) > len(message):
        return False

    elif stack[0] == message:
        return True

    # If the last value is a str we want to check if its the first character in the message
    # and if so continue matching otherwise we know its a fail
    *stack, val = stack
    if isinstance(val, str):
        return message[0] == val and match(message[1:], stack)
    # If the last value wasn't a string, we need to extend the stack based on its values in the tree, and continue the search.
    return any(match(message, stack + rule[::-1]) for rule in tree[val])


# stack is first in last out, so we need to reverse the rules order
start = tree[0][0][::-1]
print(sum(match(message, start) for message in sorted(messages.splitlines())))
tree[8] = [[42], [42, 8]]
tree[11] = [[42, 31], [42, 11, 31]]
print(sum(match(message, start) for message in sorted(messages.splitlines())))


def build_regex(node: int, depth: int) -> str:
    # Recursively check nodes in the tree, building up (ab|ba) style strings
    # until we hit a maximum depth level, really only matters for part 2, part 1 will terminate naturally, I've padded max depth just in case other peoples puzzle inputs need more.
    # I'm reusing the same tree structure as my stack based approach, which pre-parses the tree into a dict[list[list[str|int]]] tree.
    return (
        f'({"|".join("".join(sub_node if isinstance(sub_node, str) else build_regex(sub_node, depth + 1) for sub_node in branch) for branch in tree[node])})'
        if depth <= 20  # For my input 14 was enough, 20 is slower but having the deeper tree might be needed for other inputs.
        else ""
    )
    # # Longform it looks like:
    # if depth > 20:
    #     return ""
    # regex = []
    # for branch in tree[node]:
    #     b = []
    #     for sub_node in branch:
    #         if isinstance(sub_node, str):
    #             b.append(sub_node)
    #         else:
    #             b.append(build_regex(sub_node, depth + 1))
    #     regex.append("".join(b))
    # return f"({'|'.join(regex)})"


tree: dict[int, list[list[Any]]] = {
    int(k): [[int(v) if '"' not in v else v[1] for v in sub_rule.split()] for sub_rule in rule.split(" | ")] for line in rules.splitlines() for k, rule in (line.split(": "),)
}
r = re.compile(build_regex(0, 0))
print(sum(bool(r.fullmatch(m)) for m in messages.split()))

tree[8] = [[42], [42, 8]]
tree[11] = [[42, 31], [42, 11, 31]]
r = re.compile(build_regex(0, 0))
print(sum(bool(r.fullmatch(m)) for m in messages.split()))