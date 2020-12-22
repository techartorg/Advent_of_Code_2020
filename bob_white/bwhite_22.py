from collections import deque
from itertools import islice


player_01, player_02 = open("day_22.input").read().split("\n\n")
# Round 1 Fight!
p1_cards = deque(map(int, player_01.splitlines()[1:]))
p2_cards = deque(map(int, player_02.splitlines()[1:]))

while p1_cards and p2_cards:
    p1 = p1_cards.popleft()
    p2 = p2_cards.popleft()
    if p1 > p2:
        p1_cards.extend([p1, p2])
    else:
        p2_cards.extend([p2, p1])

print(sum(i * card for i, card in enumerate(reversed(p1_cards if p1_cards else p2_cards), 1)))


def recursive_combat(p1_cards, p2_cards, game=1):

    winner = 1
    existing_rounds = set()
    while p1_cards and p2_cards:
        # sets don't like deques, so we'll make tuples. So many tuples.
        current_hand = tuple(map(tuple, (p1_cards, p2_cards)))
        if current_hand in existing_rounds:
            return 1
        existing_rounds.add(current_hand)

        p1 = p1_cards.popleft()
        p2 = p2_cards.popleft()
        if len(p1_cards) < p1 or len(p2_cards) < p2:
            if p1 > p2:
                winner = 1
            else:
                winner = 2
        else:
            # Slicing a deque is complicated!
            rp1_cards = deque(islice(p1_cards, 0, p1))
            rp2_cards = deque(islice(p2_cards, 0, p2))
            winner = recursive_combat(rp1_cards, rp2_cards, game + 1)

        if winner == 1:
            p1_cards.extend([p1, p2])
        else:
            p2_cards.extend([p2, p1])

    return winner


# Recursive Combat!
p1_cards = deque(map(int, player_01.splitlines()[1:]))
p2_cards = deque(map(int, player_02.splitlines()[1:]))

winner = recursive_combat(p1_cards, p2_cards)
print(sum(i * card for i, card in enumerate(reversed(p1_cards if winner == 1 else p2_cards), 1)))
