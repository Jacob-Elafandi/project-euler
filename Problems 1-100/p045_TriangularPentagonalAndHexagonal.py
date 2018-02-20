# Triangle, pentagonal, and hexagonal numbers are generated by the
# following formulae:
#
# Triangle:     T_n=n(n+1)/2	1, 3, 6, 10, 15, ...
# Pentagonal:   P_n=n(3n−1)/2	1, 5, 12, 22, 35, ...
# Hexagonal:    H_n=n(2n−1)	    1, 6, 15, 28, 45, ...
# It can be verified that T_285 = P_165 = H_143 = 40755.
#
# Find the next triangle number that is also pentagonal and hexagonal.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from p044_PentagonNumbers import is_penta
from itertools import count

def solve():
    # All hexagonal numbers are also triangular, so we only have to
    # check hexagonal numbers until we find a pentagonal one.
    for n in count(144):
        if is_penta(n * (2 * n - 1)):
            return n * (2 * n - 1)

if __name__ == "__main__":
    start = time()
    peresult(45, solve(), time() - start)
