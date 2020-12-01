"""
--- Day 1: Report Repair ---
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island.
Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a
starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow,
you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second
puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently,
something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579,
so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply
them together?

--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from
a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same
criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together
produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
"""
from math import prod
from itertools import combinations

puzzle_inputs = [1834, 1546, 1119, 1870, 1193, 1198, 1542, 1944, 1817, 1249, 1361, 1856, 1258, 1425, 1835, 1520, 1792,
                 1130, 2004, 1366, 1549, 1347, 1507, 1699, 1491, 1557, 1865, 1948, 1199, 1229, 1598, 1756, 1643, 1306,
                 1838, 1157, 1745, 1603, 1972, 1123, 1963, 1759, 1118, 1526, 1695, 1661, 1262, 1117, 1844, 1922, 1997,
                 1630, 1337, 1721, 1147, 1848, 1476, 1975, 1942, 1569, 1126, 1313, 1449, 1206, 1722, 1534, 1706, 1596,
                 1700, 1811, 906, 1666, 1945, 1271, 1629, 1456, 1316, 1636, 1884, 1556, 1317, 1393, 1953, 1658, 2005,
                 1252, 1878, 1691, 60, 1872, 386, 1369, 1739, 1460, 1267, 1935, 1992, 1310, 1818, 1320, 1437, 1486,
                 1205, 1286, 1670, 1577, 1237, 1558, 1937, 1938, 1656, 1220, 1732, 1647, 1857, 1446, 1516, 1450, 1860,
                 1625, 1377, 1312, 1588, 1895, 1967, 1567, 1582, 1428, 1415, 1731, 1919, 1651, 1597, 1982, 1576, 1172,
                 1568, 1867, 1660, 1754, 1227, 1121, 1733, 537, 1809, 1322, 1876, 1665, 1124, 1461, 1888, 1368, 1235,
                 1479, 1529, 1148, 1996, 1939, 1340, 1531, 1438, 1897, 1152, 1321, 1770, 897, 1750, 1111, 1772, 1615,
                 1798, 1359, 1470, 1610, 1362, 1973, 1892, 1830, 599, 1341, 1681, 1572, 1873, 42, 1246, 1447, 1800,
                 1524, 1214, 1784, 1664, 1882, 1989, 1797, 1211, 1170, 1854, 1287, 1641, 1760]


def summation_equals(itr, tot, combo):
    """
    Given an iterable of floats and a desired sum total, return a tuple that matches the parameters
    :param itr: a list of floats
    :type itr: list
    :param tot: the desired total sum we are looking for
    :type tot: sum
    :param combo: The combination length for our iterator
    :type combo: int
    :return: The tuple that matches the parameters
    :rtype: tuple
    """
    return next(j for j in combinations(itr, combo) if sum(j) == tot)


def get_part_01_answer():
    """
    Static method that will return the answer to Day01.01
    :return: The product result
    :rtype: float
    """
    return prod(summation_equals(puzzle_inputs, 2020, 2))


def get_part_02_answer():
    """
    Static method that will return the answer to Day01.02
    :return: The product result
    :rtype: float
    """
    return prod(summation_equals(puzzle_inputs, 2020, 3))


