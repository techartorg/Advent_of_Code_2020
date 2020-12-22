"""

"""

player1, player2 = [line.split(':')[1].split('\n')[1:] for line in open("inputs/day22_input.txt", "r").read().split('\n\n')]

player1 = [int(num) for num in player1]
player2 = [int(num) for num in player2]


def play_standard_round(player1_card, player2_card):
    if player1_card > player2_card:
        return 1, [player1_card, player2_card]
    elif player2_card > player1_card:
        return 2, [player2_card, player1_card]


def play_recursive_round(player1_deck, player2_deck, previous_rounds):
    decks = str(','.join(str(card) for card in player1_deck)) + str(','.join(str(card) for card in player2_deck))
    if decks in previous_rounds:
        return 1
    previous_rounds.add(decks)

    player1_card = player1_deck.pop(0)
    player2_card = player2_deck.pop(0)

    # play a recursive game
    if player1_card <= len(player1_deck) and player2_card <= len(player2_deck):
        new_player1_deck = player1_deck[:player1_card]
        new_player2_deck = player2_deck[:player2_card]

        winner = play_recursive_game(new_player1_deck, new_player2_deck)

        if winner == 1:
            player1_deck.extend([player1_card, player2_card])
        elif winner == 2:
            player2_deck.extend([player2_card, player1_card])

    # play a normal round
    else:
        round_winner, round_cards = play_standard_round(player1_card, player2_card)
        if round_winner == 1:
            player1_deck.extend(round_cards)
        elif round_winner == 2:
            player2_deck.extend(round_cards)


def play_recursive_game(player1_deck, player2_deck):
    previous_rounds = set()
    while player1_deck and player2_deck:
        if play_recursive_round(player1_deck, player2_deck, previous_rounds) is not None:
            return 1

    return 1 if len(player2_deck) == 0 else 2


def part01(player1_deck, player2_deck):
    winner = 1
    while True:
        if len(player1_deck) == 0 or len(player2_deck) == 0:
            break
        winner, round_cards = play_standard_round(player1_deck.pop(0), player2_deck.pop(0))
        if winner == 1:
            player1_deck.extend(round_cards)
        elif winner == 2:
            player2_deck.extend(round_cards)
    game_deck = player1_deck if winner == 1 else player2_deck

    return 'Player {} won with a total of {}'.format(winner, sum(card*(ind+1) for ind, card in enumerate(game_deck[::-1])))


def part02(player1_deck, player2_deck):
    game_winner = play_recursive_game(player1_deck, player2_deck)
    game_deck = player1_deck if game_winner == 1 else player2_deck

    return 'Player {} won with a total of {}'.format(game_winner, sum(card*(ind+1) for ind, card in enumerate(game_deck[::-1])))


print(part01(player1[:], player2[:]))
print(part02(player1[:], player2[:]))