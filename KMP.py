# Copyright 2019 Jason Kim. All rights reserved.
# KMP.py
# My solution to KMP of the Rosalind Project.
# Jason Kim
# 7/30/2019


def main():
    file = open("rosalind_kmp.txt", "r")
    sequence = ''
    for line in file:
        if line[0] != '>':
            sequence += line.replace('\n', '')
    file.close()
    # Failure array must have the same length as the sequence
    failure_arr = [0 for x in range(len(sequence))]
    # https://stackoverflow.com/questions/13792118/kmp-prefix-table
    # Quoting for easy explanation of KMP prefix table.
    # j keeps the last length for where there was a prefix/suffix match.
    j = 0
    # i is (length of the prefix of sequence) - 1, or the last index
    # of the prefix.
    for i in range(1, len(sequence)):
        # Find j such that the last character in this prefix is equal
        # to sequence[j]. Will not run initially when j = 0.
        while j > 0 and sequence[i] != sequence[j]:
            # Backtrack a step to reduce the streak to the previous longest.
            j = failure_arr[j - 1]
        # Check if sequence[j] is now equal to the last char of prefix.
        if sequence[i] == sequence[j]:
            # If so, then the longest substring of the prefix that is both
            # a proper prefix and proper suffix of SAID prefix is one longer.
            j += 1
        # Then the len(longest matching prefix and suffix of SAID prefix denoted
        # by i) is j.
        failure_arr[i] = j
    # Print the array by spaces
    for item in failure_arr:
        print(item, end=' ')
    return


if __name__ == "__main__":
    main()

