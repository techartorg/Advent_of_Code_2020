from math import prod

from utils import grouper

sea_monster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """

TileData = tuple[tuple[bool, ...], ...]


class Tile(object):
    def __init__(self, index: int, data: TileData):
        self.index: int = index
        self.data: TileData = data
        self.connections: set[Tile] = set()

    def __repr__(self) -> str:
        return f"id: {self.index}, connections: {len(self.connections)}"

    def __eq__(self, other) -> bool:
        if isinstance(other, type(self)):
            return self.index == other.index
        return False

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash(self.index)

    def flip_h(self):
        self.data = tuple(i[::-1] for i in self.data)

    def flip_v(self):
        self.data = self.data[::-1]

    def rotate(self):
        self.data = tuple(zip(*self.data[::-1]))

    @property
    def top(self) -> tuple[bool]:
        return self.data[0]

    @property
    def bottom(self) -> tuple[bool]:
        return self.data[-1]

    @property
    def left(self) -> tuple[bool]:
        return tuple(line[0] for line in self.data)

    @property
    def right(self) -> tuple[bool]:
        return tuple(line[-1] for line in self.data)

    @property
    def edges(self) -> list[tuple[bool]]:
        return [self.top, self.bottom, self.left, self.right]


def parse_inputs() -> dict[int, Tile]:
    with open("inputs/day20.txt", 'r') as f:

        tiles: dict[int, Tile] = {}

        for tile in f.read().split("\n\n"):
            lines = tile.splitlines()
            key = int(lines[0].split(maxsplit=1)[1].replace(':', ''))
            data = tuple(tuple(c == '#' for c in line) for line in lines[1:])
            tiles[key] = Tile(key, data)

        return tiles


def can_match(lhs: Tile, rhs: Tile) -> bool:
    for start_edge in lhs.edges:
        other = rhs

        if start_edge in rhs.edges:
            return True

        for _ in range(4):
            other.rotate()
            if start_edge in other.edges:
                return True

            for _ in range(2):
                other.flip_h()
                if start_edge in other.edges:
                    return True

                for _ in range(2):
                    other.flip_v()
                    if start_edge in other.edges:
                        return True


def find_connections(tiles: dict[int, Tile]):
    for lhs in tiles.values():
        for rhs in tiles.values():
            if lhs == rhs:
                continue

            if can_match(lhs, rhs):
                lhs.connections.add(rhs)


def get_corner_edges(corner: Tile) -> list[list[Tile]]:
    if len(corner.connections) != 2:
        raise ValueError(f"starting node must have 2 connections input node has {len(corner.connections)} connections")

    edges = []

    for d in corner.connections:
        current: Tile = d
        edge: list[Tile] = [corner]

        while len(current.connections) == 3:
            edge.append(current)
            current = next((i for i in current.connections if len(i.connections) < 4 and i not in edge))
        edge.append(current)

        edges.append(edge)

    return edges


def build_map(left_edge: Tile, top_edge: Tile) -> list[list[Tile]]:
    rows = [top_edge]

    for row_index, row in enumerate(left_edge[1:], 1):
        rows.append([row])
        prev_row = rows[row_index - 1]

        current: Tile = row

        for above, next_above in grouper(prev_row, 2):
            current = next(i for i in current.connections if i != above and any(j == next_above for j in i.connections))
            rows[row_index].append(current)

    return rows


def solve() -> tuple[int, int]:
    tiles = parse_inputs()
    find_connections(tiles)
    corners = [i for i in tiles.values() if len(i.connections) == 2]

    left_edge, top_edge = get_corner_edges(corners[0])
    tile_map = build_map(left_edge, top_edge)

    return prod(i.index for i in corners), 0


a, b = solve()
print(f"part a: {a}")
print(f"part b: {b}")
