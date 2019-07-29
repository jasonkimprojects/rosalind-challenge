# Copyright 2019 Jason Kim. All rights reserved.
# PROB.py
# My solution to PROB of the Rosalind Project.
# Jason Kim
# 7/29/2019
import math


def main():
    file = open("rosalind_prob.txt", "r")
    seq = file.readline().replace('\n', '')
    gc_contents = file.readline().split(' ')
    file.close()
    for i in range(len(gc_contents)):
        gc_contents[i] = float(gc_contents[i])
    log_probability = []
    for gc in gc_contents:
        # Probability of next symbol being G/C is gc/2
        # Probability of next symbol being A/T is (1-gc)/2
        prob_gc = math.log10(gc / 2)
        prob_at = math.log10((1 - gc) / 2)
        # log(a * b) = log(a) + log(b).
        total = 0.0
        for nucleotide in seq:
            if nucleotide == 'G' or nucleotide == 'C':
                total += prob_gc
            elif nucleotide == 'A' or nucleotide == 'T':
                total += prob_at
        log_probability.append(total)
    # Print in the format Rosalind wants
    for pr in log_probability:
        print(round(pr, 3), end=' ')
    return


if __name__ == "__main__":
    main()

