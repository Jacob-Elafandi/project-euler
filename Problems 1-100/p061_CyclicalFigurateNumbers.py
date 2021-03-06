# Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal
# numbers are all figurate (polygonal) numbers and are generated by
# the following formulae:
# 
# Triangle:   n(n+1)/2	1, 3, 6, 10, 15, ...
# Square:     n^2	1, 4, 9, 16, 25, ...
# Pentagonal: n(3n−1)/2	1, 5, 12, 22, 35, ...
# Hexagonal:  n(2n−1)	1, 6, 15, 28, 45, ...
# Heptagonal: n(5n−3)/2	1, 7, 18, 34, 55, ...
# Octagonal:  n(3n−2)	1, 8, 21, 40, 65, ...
# 
# The ordered set of three 4-digit numbers: 8128, 2882, 8281, has
# three interesting properties.
# 
# The set is cyclic, in that the last two digits of each number is the first
# two digits of the next number (including the last number with the first).
# Each polygonal type: triangle (8128), square (8281), and
# pentagonal (2882), is represented by a different number in the set.
# This is the only set of 4-digit numbers with this property.
# Find the sum of the only ordered set of six cyclic 4-digit numbers for
# which each polygonal type: triangle, square, pentagonal, hexagonal,
# heptagonal, and octagonal, is represented by a different number in the set.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
    start = time()
    maps = [dict() for x in range(6)]
    for digitPair in range(100):
        for i in range(len(maps)):
            maps[i][digitPair] = []
    n = 1
    while n * (n+1) // 2 < 10**4:
        polynums = [n * (n+1) // 2,     \
                    n ** 2,             \
                    n * (3*n - 1) // 2, \
                    n * (2*n - 1),      \
                    n * (5*n - 3) // 2, \
                    n * (3*n - 2)]
        for i in range(len(polynums)):
            if 10**3 < polynums[i] < 10**4:
                maps[i][polynums[i] // 100].append(polynums[i] % 100)
        n += 1
    permutes = []
    for a in range(5): #I could do this synthetically, but this is easier
        for b in range(5):
            for c in range(5):
                for d in range(5):
                    for e in range(5):
                        if len({a, b, c, d, e}) == 5:
                            permutes.append((a, b, c, d, e))
    for permute in permutes:
        paths = []
        for key in maps[5].keys():
            if len(maps[5][key]) > 0:
                paths.append([key, maps[5][key][0]])
        #That works because no octagonal num starts w/ same 2 digits
        for step in range(5):
            newpaths = []
            for path in paths:
                key = path[-1]
                if key in maps[permute[step]].keys():
                    for nextStep in maps[permute[step]][key]:
                        newpaths.append(path + [nextStep])
            paths = newpaths
        for goodpath in paths:
            if goodpath[0] == goodpath[-1]:
                result = 0
                for i in range(0, len(goodpath) - 1):
                    result += (goodpath[i] * 100) + goodpath[i+1]
                peresult(61, result, time() - start)
                return
    print("Error: Program fell through without finding good path")

if __name__ == "__main__":
    solve()
