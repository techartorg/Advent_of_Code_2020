pzl_input = list(map(int, open("day_15.input").read().split(",")))
# Starting one early so we can peak at the previous spoken value.
spoken = {v: idx for idx, v in enumerate(pzl_input, 1)}
prev_num = num = pzl_input[-1]
for turn in range(len(spoken), 30_000_001):
    # Because turn is the last time the word was spoken, we only need to store one value, not two.
    num = turn - spoken[prev_num] if prev_num in spoken else 0
    spoken[prev_num] = turn
    if turn == 2020:
        print(prev_num)
    elif turn == 30_000_000:
        print(prev_num)
    prev_num = num