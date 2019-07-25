# Copyright 2019 Jason Kim. All rights reserved.
# LIA.py
# My solution to LIA of the Rosalind Project.
# Jason Kim
# 7/25/2019
import math


# Helper function for calculating the binomial coefficient.
def ncr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))


# Helper function for calculating the probability of exactly x
# individuals having genotype AaBb in the kth generation.
def prob(k, x):
    return ncr(2**k, x) * (0.25**x) * (0.75**(2**k - x))


def main():
    file = open("rosalind_lia.txt", "r")
    params = file.readline().split(' ')
    k = int(params[0])
    n = int(params[1])
    file.close()
    # Pr(AaBb offspring) = Pr(Aa offspring) * Pr(Bb offspring)
    # Due to Mendel's Law of Independent Assortment.
    # Pr(Aa offspring) = Pr(Aa mate * ?? parent -> Aa offspring).
    # This problem is solvable because the probability of yielding
    # Aa offspring from an Aa parent and a parent of unknown genotype
    # is always 0.5 (draw the Punnett squares with AA, Aa, aa).
    # In the same way, the probability of yielding Bb offspring from a
    # Bb parent and a parent of unknown genotype is also 0.5 regardless
    # of the unknown parent's genotype (BB, Bb, bb).
    # Therefore, Pr(AaBb offspring) = 0.5 * 0.5 = 0.25.
    # The kth generation will have 2^k individuals since the assumption
    # is that every pair of parents will have two offspring.
    # The probability that EXACTLY x individuals will have genotype
    # AaBb out of 2^k total individuals is
    # nCr(2^k, x) * 0.25^x * (1-0.25)^(2^k - x)
    # Since having an AaBb offspring (or not) is a Bernoulli trial
    # and thus it follows the binomial distribution.
    # This is implemented as the helper functions ncr and prob.
    # Since the answer is the probability that at least n organisms
    # Have genotype AaBb, use the complement rule. The answer is equal to
    # 1 - (Pr(0 organisms) + Pr(1 organism) +...+ Pr(n-1 organisms)).
    total = 0.0
    for i in range(n):
        # i ranges from 0 to n-1
        total += prob(k, i)
    # Again, the answer is the complement.
    print(round(1 - total, 3))
    return


if __name__ == "__main__":
    main()

