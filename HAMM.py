# Copyright 2019 Jason Kim. All rights reserved.
# HAMM.py
# My solution to HAMM of the Rosalind Project.
# Jason Kim
# 7/24/2019


def main():
    file = open("rosalind_hamm.txt", "r")
    sequences = file.readlines()
    # Check assumption that sequence lengths are equal.
    assert len(sequences[0]) == len(sequences[1])
    hamming_dist = 0
    for i in range(len(sequences[0])):
        if sequences[0][i] != sequences[1][i]:
            hamming_dist += 1
    print(hamming_dist)
    file.close()
    return


if __name__ == "__main__":
    main()

