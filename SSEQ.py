# Copyright 2019 Jason Kim. All rights reserved.
# SSEQ.py
# My solution to SSEQ of the Rosalind Project.
# Jason Kim
# 7/29/2019


# Helper function to find a char in a string after
# some given index.
def find_after(string, char, index):
    return string[index:].find(char)


def main():
    file = open("rosalind_sseq.txt", "r")
    sequences = []
    buffer = ''
    for line in file:
        if line[0] == '>':
            if buffer:
                sequences.append(buffer)
                buffer = ''
        else:
            buffer += line.replace('\n', '')
    # Add last buffer manually
    sequences.append(buffer)
    # sequences[0] has the string, sequences[1] has the substring
    indices = []
    for i in range(len(sequences[1])):
        # Starting index is 0 for the first subsequence, or the index of
        # the occurrence of the last char in substr for all others.
        start_idx = 0
        if i != 0:
            start_idx = indices[i - 1]
        # Find where the char is, after the index where the last find occurred
        partial_idx = find_after(sequences[0], sequences[1][i], start_idx)
        assert partial_idx >= 0
        # Rosalind wants 1-based indices
        indices.append(start_idx + partial_idx + 1)
    for item in indices:
        print(item, end=' ')
    return


if __name__ == "__main__":
    main()

