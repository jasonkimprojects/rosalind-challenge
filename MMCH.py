# Copyright 2019 Jason Kim. All rights reserved.
# MMCH.py
# My solution to MMCH of the Rosalind Project.
# Jason Kim
# 7/31/2019
import math


# Helper function to return permutations of r objects in a set of n.
# I.e. returns n! / (n-r)!
def npr(n, r):
    # Sanity check.
    assert n >= r
    return math.factorial(n) // math.factorial(n - r)


def main():
    file = open("rosalind_mmch.txt", "r")
    seq = ''
    for line in file:
        if line[0] != '>':
            seq += line.replace('\n', '')
    file.close()
    # Count the number of A, U, G, C.
    # Array indices are in this order, so arr[0] = number of A,
    # arr[1] = number of U, arr[2] = number of G, arr[3] = number of C.
    arr = [0 for i in range(4)]
    for char in seq:
        if char == 'A':
            arr[0] += 1
        elif char == 'U':
            arr[1] += 1
        elif char == 'G':
            arr[2] += 1
        elif char == 'C':
            arr[3] += 1
    # Since edges in this graph can overlap, the pairings between
    # (A,U) and (G,C) in this graph are independent of each other.
    # Therefore, the number of maximum matchings =
    # max matchings of (A,U) * max matchings of (G,C).
    # Then consider the case of matchings As to Us.
    # The number of A-U maximum matchings is nPr(U, A) if U > A and
    # nPr(A, U) if A > U.
    # Similarly, the number of G-C maximum matchings is nPr(C, G) if
    # C > G and nPr(G, C) if G > C.
    # If A=U or G=C, use either one - it just becomes the factorial.
    max_au_matchings = 0
    max_gc_matchings = 0
    if arr[0] >= arr[1]:
        max_au_matchings = npr(arr[0], arr[1])
    else:
        max_au_matchings = npr(arr[1], arr[0])
    if arr[2] >= arr[3]:
        max_gc_matchings = npr(arr[2], arr[3])
    else:
        max_gc_matchings = npr(arr[3], arr[2])
    print(max_au_matchings * max_gc_matchings)


if __name__ == "__main__":
    main()

