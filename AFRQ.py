# Copyright 2019 Jason Kim. All rights reserved.
# AFRQ.py
# My solution to AFRQ of the Rosalind Project.
# Jason Kim
# 8/7/2019
import math
'''
According to the Hardy-Weinberg Principle:
p = frequency of dominant allele
q = frequency of recessive allele
p + q = 1 and p^2 + 2pq + q^2 = 1, where:
p^2 = frequency of homozygous dominant (p*p)
2pq = frequency of homozygous (p*q + q*p)
q^2 = frequency of homozygous recessive (q*q)
Therefore frequency of individual carrying at least 1
copy of recessive allele q = 2pq + q^2.
'''


def main():
    file = open("rosalind_afrq.txt", "r")
    q_squares = list(map(float, file.readline().strip().split(' ')))
    for q_square in q_squares:
        q = math.sqrt(q_square)
        p = 1 - q
        print(round(2*p*q + q**2, 3), end=' ')
    return


if __name__ == "__main__":
    main()

