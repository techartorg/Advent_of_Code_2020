input_ = '''Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
'''

import copy
import re

#location = __file__
#input_ = open(location.replace('.py', '_input.txt')).read()

class Tile():
    def __init__(self, rawData):
        self.tileId = None
        self.imageData = []
        self.imageData2 = []
        self.parse_raw_data(rawData)
        self.neighbors = []

    def parse_raw_data(self, rawData):
        rawData = rawData.splitlines()

        tileId = rawData[0]
        m = re.search(r'[0-9]+', tileId)
        self.tileId = int(m.group(0))

        imageData = rawData[1:]
        self.imageData = [list(x) for x in imageData]
    
    def get_top_edge(self):
        return self.imageData[0]

    def get_bottom_edge(self):
        return self.imageData[-1]

    def get_left_edge(self):
        return [item[0] for item in self.imageData] 

    def get_right_edge(self):
        return [item[-1] for item in self.imageData]
    
    def print_data(self):
        """Debug prints the input data."""
        lines = [''.join(x) for x in self.imageData]
        data = '\n'.join(lines)
        print(data)

    def print_data2(self):
        """Debug prints the stripped data for part 2."""
        lines = [''.join(x) for x in self.imageData2]
        data = '\n'.join(lines)
        print(data)
    
    def strip_borders(self):
        """Removes the border data used for matching tiles."""
        self.imageData2 = copy.deepcopy(self.imageData)
        # Remove the first and last rows first.
        self.imageData2.pop(0)
        self.imageData2.pop()
        # For each row, remove the first last columns.
        for row in self.imageData2:
            row.pop(0)
            row.pop()

    def flip_vertical(self):
        # Flips self.imageData2 vertically.
        self.imageData2 = self.imageData2[::-1]

    def flip_horizontal(self):
         # Flips self.imageData2 horizontally.
        self.imageData2 = [x[::-1] for x in self.imageData2]
    
    def rotate_180(self):
        # Flip both vertically and horizontally to rotate 180.
        self.flip_vertical()
        self.flip_horizontal()
    
    def rotate_90_clockwise(self):
        # Rotate self.imageData2 90 degrees clockwise.
        self.imageData2 = list(zip(*self.imageData2[::-1]))
    
    def rotate_90_counter_clockwise(self):
        # Rotate self.imageData2 90 degrees counter clockwise.
        self.imageData2 = list(zip(*self.imageData2))[::-1]

    @property
    def borders(self):
        """Returns the borders clockwise from the top.
        Top, Right, Bottom, Left.
        """
        return [self.get_top_edge(), 
                self.get_right_edge(), 
                self.get_bottom_edge(), 
                self.get_left_edge()]

    @property
    def neighborCount(self):
        return len(self.neighbors)
    
    @classmethod
    def flip_edge(cls, dataSet):
        return dataSet[::-1]
    
    @classmethod
    def edges_match(cls, edge0, edge1):
        # Compare if the edges match, if they don't,
        # then try flipping the edge to see if there is
        # match.
        if edge0 == edge1:
            return True
        else:
            if edge0 == Tile.flip_edge(edge1):
                return True
            return False


def compare_tiles(tile0, tile1):
    """Given two tiles, determine if any of their
    borders match. The tiles may be flipped or rotated,
    so we need to test each border of tile1 against
    each border of tile0."""
    borders0 = tile0.borders
    borders1 = tile1.borders
    for b0 in borders0:
        for b1 in borders1:
            if Tile.edges_match(b0, b1):
                tile0.neighbors.append(tile1)
                tile1.neighbors.append(tile0)
                return

def part1():
    tiles = []

    for dataSet in input_.split('\n\n'):
        tiles.append(Tile(dataSet))
    
    tileCount = len(tiles)
    for i in range(tileCount):
        for j in range(i+1, tileCount):
            compare_tiles(tiles[i], tiles[j])

    result = 1
    for t in tiles:
        if t.neighborCount == 2:
            result *= t.tileId
    return result


print(part1())

"""
def part2():
    tiles = []

    for dataSet in input_.split('\n\n'):
        tiles.append(Tile(dataSet))
    
    for t in tiles:
        t.strip_borders()
        #t.print_data2()
    
    tiles[0].print_data2()
    print('\n')
    tiles[0].rotate_90_counter_clockwise()
    tiles[0].print_data2()

part2()
"""
