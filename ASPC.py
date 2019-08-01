# Copyright 2019 Jason Kim. All rights reserved.
# ASPC.py
# My solution to ASPC of the Rosalind Project.
# Jason Kim
# 8/1/2019
import math


# Helper function to return the binomial coefficient.
def ncr(n, r):
    assert n >= r
    return math.factorial(n) // (math.factorial(r) *
                                 math.factorial(n - r))


def main():
    file = open("rosalind_aspc.txt", "r")
    data = file.readline().strip().split(' ')
    file.close()
    n = int(data[0])
    m = int(data[1])
    total = 0
    for k in range(m, n + 1):
        total += ncr(n, k)
    print(total % 1000000)
    return


if __name__ == "__main__":
    main()

