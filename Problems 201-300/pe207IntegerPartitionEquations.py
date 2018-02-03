##For some positive integers k, there exists an integer partition of the form
##4^t = 2^t + k,
##where 4t, 2t, and k are all positive integers and t is a real number.
##
##The first two such partitions are 41 = 21 + 2 and
##41.5849625... = 21.5849625... + 6.
##
##Partitions where t is also an integer are called perfect.
##For any m ≥ 1 let P(m) be the proportion of such partitions that are perfect
##with k ≤ m.
##Thus P(6) = 1/2.
##
##In the following table are listed some values of P(m)
##
##   P(5) = 1/1
##   P(10) = 1/2
##   P(15) = 2/3
##   P(20) = 1/2
##   P(25) = 1/2
##   P(30) = 2/5
##   ...
##   P(180) = 1/4
##   P(185) = 3/13
##
##Find the smallest m for which P(m) < 1/12345

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(denom):
    start = time()
    goodratio = 1/denom
    t = 1
    while True:
        t += 1
        ratio = (t-1)/(2**t - 2)
        if ratio < goodratio:
            n = (t - 1) * denom + 2
            result = n ** 2 - n
            break
    peresult(207, result, time() - start)

if __name__ == "__main__":
    solve(12345)