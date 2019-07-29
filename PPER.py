# Copyright 2019 Jason Kim. All rights reserved.
# PPER.py
# My solution to PPER of the Rosalind Project.
# Jason Kim
# 7/29/2019


# Returns the nPr(n, r).
# Prevents overflow with 32-bit integers.
# Since if a*b == c, then a (mod N) * b (mod N) === c (mod N)
def safe_npr(n, r):
    result = 1
    for i in range(n, n - r, -1):
        result = (result * i) % 1000000
    return result


def main():
    file = open("rosalind_pper.txt", "r")
    params = file.readline().split(' ')
    file.close()
    n = int(params[0])
    k = int(params[1])
    # nPr(n, r) = n! / (n - r)!
    print(safe_npr(n, k))
    return


if __name__ == "__main__":
    main()

