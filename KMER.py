# Copyright 2019 Jason Kim. All rights reserved.
# KMER.py
# My solution to KMER of the Rosalind Project.
# Jason Kim
# 7/30/2019


def main():
    # There are 256 possible 4-mers, because each "mer" has
    # 4 choices of [A, C, G, T] therefore 4^4 = 256.
    # The hash table four_mers stores keys of 4-mers and
    # values of how many times the 4-mer indicated by the key
    # occurs in the DNA sequence.
    four_mers = {}
    bases = "ACGT"
    # Make a four-nested for loop to add the 4-mers to the
    # hash table in lexicographical order.
    for base1 in bases:
        for base2 in bases:
            for base3 in bases:
                for base4 in bases:
                    four_mer = base1 + base2 + base3 + base4
                    four_mers[four_mer] = 0
    # Sanity check.
    assert len(four_mers) == 256
    file = open("rosalind_kmer.txt", "r")
    sequence = ''
    for line in file:
        if line[0] != '>':
            sequence += line.replace('\n', '')
    file.close()
    # Iterate over every 4-base window in the sequence.
    for i in range(len(sequence) - 3):
        four_mer = sequence[i:i + 4]
        # Another sanity check - make sure the sequence is valid
        assert (four_mer in four_mers)
        # Increment value in hash table
        four_mers[four_mer] += 1
    # Print in spaced format in lexicographical order
    for key in four_mers:
        print(four_mers[key], end=' ')
    return


if __name__ == "__main__":
    main()

