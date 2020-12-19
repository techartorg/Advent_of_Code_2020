from pprint import pprint
from re import match

rules, messages = open("day_19.input").read().split("\n\n")
tree = {
    int(k): [list(map(int, x.split(" "))) for x in rest.split(" | ")] if '"' not in rest else [[rest[1]]] for line in rules.splitlines() for k, rest in (line.split(": "),)
}


def match(message, stack):
    # We know we can't match if we run out of stack, or our stack grows past the length of the message.
    if len(stack) > len(message) or not stack:
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
print(sum(match(message, start) for message in messages.splitlines()))
tree[8] = [[42], [42, 8]]
tree[11] = [[42, 31], [42, 11, 31]]
print(sum(match(message, start) for message in messages.splitlines()))
