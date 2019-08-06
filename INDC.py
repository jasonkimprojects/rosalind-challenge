# Copyright 2019 Jason Kim. All rights reserved.
# INDC.py
# My solution to INDC of the Rosalind Project.
# Jason Kim
# 8/6/2019
import math


# Helper function to calculate the binomial coefficient.
def ncr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


def main():
    file = open("rosalind_indc.txt", "r")
    n = int(file.readline().strip())
    file.close()
    '''
    For each of the 2n chromosomes, they must have come from
    the gametes of the same parent. The parent has two choices for
    each gamete: pass down the chromosome from the parent's mother,
    or pass down the chromosome from the parent's father.
    So for two gametes, the possible combinations are:
    (mother, mother), (father, father), (mother, father), (father, mother)
    Only the first two cases yield siblings that share the chromosome,
    so the probability of two siblings sharing a chromosome = 2/4 = 0.5
    '''
    pr_share = 0.5
    for i in range(1, 2*n + 1):
        total = 0.0
        for j in range(i, 2*n + 1):
            # Pr(exactly j matches) = C(2n, j)*p^j*(1-p)^(2n-j)
            # For some reason, direct sum turns out being more accurate
            # than using the complement rule.
            # Since this is for all i, the computation cost for direct sum
            # and complement rule are the same in the end.
            total += ncr(2*n, j) * (pr_share**j) * ((1-pr_share)**(2*n - j))
        print(round(math.log10(total), 3), end=' ')
    return


if __name__ == "__main__":
    main()

