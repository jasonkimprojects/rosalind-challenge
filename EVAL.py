# Copyright 2019 Jason Kim. All rights reserved.
# EVAL.py
# My solution to EVAL of the Rosalind Project.
# Jason Kim
# 8/1/2019
import math


def ncr(n, r):
    assert n >= r
    return math.factorial(n) // (math.factorial(r) *
                                 math.factorial(n - r))


def main():
    file = open("rosalind_eval.txt", "r")
    random_strlen = int(file.readline().strip())
    substr = file.readline().strip()
    gc_contents = map(float, file.readline().strip().split(' '))
    file.close()
    for gc in gc_contents:
        # Probability of G or C is gc/2 each.
        prob_gc = gc / 2
        # Probability of A or T is (1-gc)/2 each.
        prob_at = (1 - gc) / 2
        # Now use those probabilities, multiply them
        # together since each base in substr is indep.
        # of each other, to get the probability of
        # getting substr.
        prob_substr = 1
        for char in substr:
            if char == 'G' or char == 'C':
                prob_substr *= prob_gc
            elif char == 'A' or char == 'T':
                prob_substr *= prob_at
        # There are random_strlen - len(substr) + 1 positions
        # in the random string for which substr can fit inside
        # it as a substring. Call this number P.
        p = random_strlen - len(substr) + 1
        # Then this problem is a binomial random variable.
        # If, during the p windows which substr can fit in,
        # if substr is a substring then it is a success, otherwise
        # a fail. Then the expected value is p trials * prob_substr
        # since prob_substr is the probability of a success.
        print(round(prob_substr * p, 3), end=' ')
    return


if __name__ == "__main__":
    main()

