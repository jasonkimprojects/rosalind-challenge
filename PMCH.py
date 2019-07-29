# Copyright 2019 Jason Kim. All rights reserved.
# PMCH.py
# My solution to PMCH of the Rosalind Project.
# Jason Kim
# 7/29/2019
import math


def main():
    file = open("rosalind_pmch.txt", "r")
    lines = file.readlines()
    file.close()
    # Discard tag, append everything else to sequence.
    seq = ''
    for line in lines:
        if line[0] != '>':
            seq += line.replace('\n', '')
    # Store the number of A--U base pairs and G---C base pairs
    # separately. Since edges in E can be formed only between {A, U}
    # and {C, G}, they can be treated as two independent graphs.
    num_au = 0
    num_gc = 0
    # Parse seq to count base pairs.
    # Since the precondition is that num(A) == num(U) and
    # num(C) == num(G), both numbers will ALWAYS be even.
    for nucleotide in seq:
        if nucleotide == 'A' or nucleotide == 'U':
            num_au += 1
        elif nucleotide == 'G' or nucleotide == 'C':
            num_gc += 1
    # The graph consisting of vertices A and U has num_au / 2 As
    # and num_au / 2 Gs. Therefore, for a perfect matching, the
    # first vertex (doesn't matter which nucleotide you start at)
    # has num_au / 2 choices. The second vertex has (num_au / 2 ) - 1
    # choices, all the way to the last vertex which is left with 1 choice.
    # In other words, # of perfect matchings per independent graph =
    # (num_au / 2)! This works the same way for the graph of G and C.
    au_perfect_matchings = math.factorial(num_au / 2)
    gc_perfect_matchings = math.factorial(num_gc / 2)
    # Since the AU and GC graphs are independent, the total # of perfect
    # matchings is simply their product.
    print(au_perfect_matchings * gc_perfect_matchings)
    return


if __name__ == "__main__":
    main()

