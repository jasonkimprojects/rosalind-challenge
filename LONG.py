# Copyright 2019 Jason Kim. All rights reserved.
# LONG.py
# My solution to LONG of the Rosalind Project.
# Jason Kim
# 7/26/2019


# Helper function that returns the number of chars
# in the overlap between two strings, as well as
# the fused string itself.
def overlap(str1, str2):
    max_overlap = -1
    overlap_str = ''
    # Case 1: suffix of str1 = prefix of str2
    for i in range(min(len(str1), len(str2))):
        if str1[len(str1) - i:] == str2[:i]:
            if i > max_overlap:
                max_overlap = i
                overlap_str = str1 + str2[i:]
    # Case 2: suffix of str2 = prefix of str1
    for j in range(min(len(str2), len(str1))):
        if str2[len(str2) - j:] == str1[:j]:
            if j > max_overlap:
                max_overlap = j
                overlap_str = str2 + str1[j:]
    # Compound return
    return max_overlap, overlap_str


def main():
    file = open("rosalind_long.txt", "r")
    lines = file.readlines()
    file.close()
    fragments = []
    buffer = ''
    for line in lines:
        if line[0] == '>':
            if buffer:
                fragments.append(buffer)
            buffer = ''
        else:
            buffer += line.replace('\n', '')
    # Append last buffer manually
    fragments.append(buffer)
    # Approximate greedy algorithm: repeat until
    # only one fragment is remaining.
    while len(fragments) > 1:
        # Search for the pair of fragments with the most overlap,
        # where overlap is defined as suffix of str1 = prefix of str2
        # or suffix of str2 = prefix of str1.
        most_overlap = -1
        most_overlap_str = ''
        most_overlap_i = ''
        most_overlap_j = ''
        for i in range(len(fragments) - 1):
            for j in range(i + 1, len(fragments)):
                overlap_chars, fused_str = overlap(fragments[i], fragments[j])
                if overlap_chars > most_overlap:
                    most_overlap = overlap_chars
                    most_overlap_str = fused_str
                    most_overlap_i = fragments[i]
                    most_overlap_j = fragments[j]
        # Done searching for most overlapping pair, and we already
        # have computed the fused string.
        # Delete the pair from the fragments, and add the fused string.
        fragments.pop(fragments.index(most_overlap_i))
        fragments.pop(fragments.index(most_overlap_j))
        fragments.append(most_overlap_str)
    print(fragments[0])
    return


if __name__ == "__main__":
    main()

