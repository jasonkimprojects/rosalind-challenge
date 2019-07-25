# Copyright 2019 Jason Kim. All rights reserved.
# MRNA.py
# My solution to MRNA of the Rosalind Project.
# Jason Kim
# 7/25/2019


def main():
    # Dictionary to keep track of how many codons
    # respond to each amino acid (single-letter code).
    # Sanity check: 20 amino acids, total 61 codons.
    # (The remaining 3 codons are STOP codons.)
    num_codons = {
        'F': 2,
        'L': 6,
        'S': 6,
        'Y': 2,
        'C': 2,
        'W': 1,
        'P': 4,
        'H': 2,
        'Q': 2,
        'R': 6,
        'I': 3,
        'M': 1,
        'T': 4,
        'N': 2,
        'K': 2,
        'V': 4,
        'A': 4,
        'D': 2,
        'E': 2,
        'G': 4
    }
    file = open("rosalind_mrna.txt", "r")
    sequence = file.readline()
    sequence = sequence.replace('\n', '')
    file.close()
    # Multiplier will be modulo-ed by one million
    # in order to prevent overflow.
    # Keeping just the modulo yields the same answer due to
    # the multiplicative property of modular arithmetic.
    mult = 1
    for char in sequence:
        mult = (mult * num_codons[char]) % 1000000
    # Multiply the result by 3 then modulo again,
    # Because there are 3 possible codons to stop translation.
    # This is the final answer.
    mult = (mult * 3) % 1000000
    print(mult)
    return


if __name__ == "__main__":
    main()

