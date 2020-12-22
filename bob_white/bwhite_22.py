from collections import defaultdict, deque


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


p1_cards = deque(map(int, player_01.splitlines()[1:]))
p2_cards = deque(map(int, player_02.splitlines()[1:]))

existing_rounds = defaultdict(set)


def recursive_combat(p1_cards, p2_cards, game=1):

    winner = 1
    while p1_cards and p2_cards:
        # sets don't like deques, so we'll make tuples. So many tuples.
        current_hand = tuple(map(tuple, (p1_cards, p2_cards)))
        if current_hand in existing_rounds[game]:
            return 1
        existing_rounds[game].add(current_hand)

        p1 = p1_cards.popleft()
        p2 = p2_cards.popleft()
        if len(p1_cards) < p1 or len(p2_cards) < p2:
            if p1 > p2:
                winner = 1
            else:
                winner = 2
        else:
            # Can't slice a deque, so we have to list and slice,
            # though I guess we could copy, and pop from the bottom
            rp1_cards = deque(list(p1_cards)[:p1])
            rp2_cards = deque(list(p2_cards)[:p2])
            # This should in theory get us a unique game-id for each call.
            # otherwise spawning multiple sub-games from the same game-name would reuse the id
            winner = recursive_combat(rp1_cards, rp2_cards, max(existing_rounds) + 1)

        if winner == 1:
            p1_cards.extend([p1, p2])
        else:
            p2_cards.extend([p2, p1])

    return winner


winner = recursive_combat(p1_cards, p2_cards)
print(sum(i * card for i, card in enumerate(reversed(p1_cards if winner == 1 else p2_cards), 1)))
