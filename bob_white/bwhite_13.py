from operator import mul
from collections import deque

time, buses = open("day_13.input").read().splitlines()

bus_ids = [(idx, int(bus)) for idx, bus in enumerate(buses.split(",")) if bus != "x"]
closest = [((int(time) // bus) * bus - int(time) + bus, bus) for _, bus in bus_ids]
print(f"Part 01: {mul(*min(closest))}")


bus_deque = deque(bus_ids)
t, step = bus_deque.popleft()
while bus_deque:
    offset, next_step = bus_deque[0]
    # Keep stepping foward by the next multiple of our busses.
    if (t + offset) % next_step:
        t += step
    else:
        # Remainder is zero, so we've found the next offset, need to up our step value by the next_step, and grab the next
        # Luckily all the bus_ids are prime, so we can just keep multilying the step values together.
        # otherwise we'd need to find the least common multipler so that we don't accidently overshoot.
        step *= next_step
        bus_deque.popleft()

print(f"Part 02: {t}")
