# Copyright 2019 Jason Kim. All rights reserved.
# PDST.py
# My solution to PDST of the Rosalind Project.
# Jason Kim
# 7/31/2019


# Returns the p-distance between two sequences.
def p_dist(first, second):
    # Sanity check
    assert len(first) == len(second)
    # Then calculate the Hamming distance.
    hamming_dist = 0
    for i in range(len(first)):
        if first[i] != second[i]:
            hamming_dist += 1
    # p-dist = Hamming / length of sequences
    return hamming_dist / len(first)


def main():
    file = open("rosalind_pdst.txt", "r")
    sequences = []
    buffer = ''
    for line in file:
        if line[0] == '>':
            if buffer:
                sequences.append(buffer)
                buffer = ''
        else:
            buffer += line.replace('\n', '')
    sequences.append(buffer)
    # Let n be the number of sequences in the file.
    # Then the distance matrix is an n x n matrix.
    dm = [[0.0 for i in range(len(sequences))] for j in range(len(sequences))]
    # Then iterate pairwise, excluding itself.
    for x in range(len(sequences)):
        for y in range(len(sequences)):
            if x != y:
                dm[x][y] = p_dist(sequences[x], sequences[y])
    # Print in Rosalind's format
    for row in dm:
        for num in row:
            print(round(num, 5), end=' ')
        print()
    return


if __name__ == "__main__":
    main()

