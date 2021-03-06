# The following iterative sequence is defined for the
# set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate
# the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and
# finishing at 1) contains 10 terms. Although it has not
# been proved yet (Collatz Problem), it is thought that all
# starting numbers finish at 1.
#
# Which starting number, under one million, produces the
# longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go
# above one million.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(cap = 1000000):
    stepstoend = {1: 1}
    longest = 0
    longest_start = 0
    for x in range(2, cap + 1):
        sequence = [x]
        while sequence[-1] not in stepstoend.keys():
            if sequence[-1] % 2 == 1:
                sequence.append(3 * sequence[-1] + 1)
            else:
                sequence.append(sequence[-1] // 2)
        for step in range(1, len(sequence)):
            stepstoend[sequence[-1-step]] = stepstoend[sequence[-1]] + step
        if stepstoend[x] > longest:
            longest = stepstoend[x]
            longest_start = x
    return longest_start

if __name__ == "__main__":
    start = time()
    peresult(14, solve(), time() - start)
