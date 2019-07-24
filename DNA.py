# Copyright 2019 Jason Kim. All rights reserved.
# DNA.py
# My solution to DNA of the Rosalind Project.
# Jason Kim
# 7/23/2019


def main():
    file = open("rosalind_dna.txt", "r")
    dna_string = file.read()
    nucleotides = [0, 0, 0, 0]
    for char in dna_string:
        if char == 'A':
            nucleotides[0] += 1
        elif char == 'C':
            nucleotides[1] += 1
        elif char == 'G':
            nucleotides[2] += 1
        elif char == 'T':
            nucleotides[3] += 1
    for base in nucleotides:
        print(base, end=' ')
    file.close()
    return


if __name__ == "__main__":
    main()

