from operator import mul
from collections import deque
from math import gcd

time, buses = open("day_13.input").read().splitlines()

bus_ids = [(idx, int(bus)) for idx, bus in enumerate(buses.split(",")) if bus != "x"]
closest = [((int(time) // bus) * bus - int(time) + bus, bus) for _, bus in bus_ids]
print(f"Part 01: {mul(*min(closest))}")


bus_deque = deque(bus_ids)
t, step = bus_deque.popleft()
while bus_deque:
    idx, bus_id = bus_deque[0]
    # Keep steping foward by the next multiple of our busses.
    if (t + idx) % bus_id:
        t += step
    else:
        # When the remainder is zero, we can add a new bus to the system
        # so we need to get a new LCM - least common multiple from our old
        # time step, and the new bus_id
        # Then we can pop off a new bus and work our way through the list.
        step = abs(step * bus_id) // gcd(step, bus_id)
        bus_deque.popleft()

print(f"Part 02: {t}")
