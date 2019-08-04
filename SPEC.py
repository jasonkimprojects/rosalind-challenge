# Copyright 2019 Jason Kim. All rights reserved.
# SPEC.py
# My solution to SPEC of the Rosalind Project.
# Jason Kim
# 8/4/2019


def main():
    # Simplified monoisotopic mass table rounded to the
    # decimal point (no decimals), for easier hashing.
    # For amino acids whose weights only differ below the
    # decimal point, they have been consolidated into one.
    amino_acids = {
        'A': 71.03711,
        'C': 103.00919,
        'D': 115.02694,
        'E': 129.04259,
        'F': 147.06841,
        'G': 57.02146,
        'H': 137.05891,
        'I': 113.08406,
        'K': 128.09496,
        'L': 113.08406,
        'M': 131.04049,
        'N': 114.04293,
        'P': 97.05276,
        'Q': 128.05858,
        'R': 156.10111,
        'S': 87.03203,
        'T': 101.04768,
        'V': 99.06841,
        'W': 186.07931,
        'Y': 163.06333
    }
    file = open("rosalind_spec.txt", "r")
    weights = []
    for line in file:
        weights.append(float(line.strip()))
    file.close()
    # Now calculate differences between each
    # adjacent pair of weights.
    diffs = []
    for i in range(len(weights) - 1):
        diffs.append(weights[i + 1] - weights[i])
    for num in diffs:
        # For each num, find the amino acid
        # that has the smallest difference between
        # its mass and num.
        closest_char = ''
        difference = 200.0
        for key, value in amino_acids.items():
            delta = abs(num - value)
            if delta < difference:
                difference = delta
                closest_char = key
        print(closest_char, end='')
    return


if __name__ == "__main__":
    main()

