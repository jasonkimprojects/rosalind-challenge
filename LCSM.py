# Copyright 2019 Jason Kim. All rights reserved.
# LCSM.py
# My solution to LCSM of the Rosalind Project.
# Jason Kim
# 7/24/2019
import sys


def main():
    # Find the shortest sequence to do less calculations,
    # Since the longest substring must be a substring
    # of the shortest sequence as well.
    idx = 0
    min_len = sys.maxsize
    min_len_idx = -1
    file = open("rosalind_lcsm.txt", "r")
    data = []
    buffer = ''
    for line in file:
        line = line.replace('\n', '')
        if line[0] == '>':
            # Empty sequences evaluate to false.
            if buffer:
                # Buffer is not empty. Check length.
                if len(buffer) < min_len:
                    min_len = len(buffer)
                    min_len_idx = idx
                data.append(buffer)
                # Increment index counter after append.
                idx += 1
            buffer = ''
        else:
            buffer += line
    # Append the last sequence manually
    # because there are no more name tags with >
    if len(buffer) < min_len:
        min_len = len(buffer)
        min_len_idx = idx
    data.append(buffer)
    idx += 1
    file.close()
    # Keep track of the longest substring.
    longest_substr = ''
    # Generate substrings of the shortest sequence.
    for start in range(min_len):
        for end in range(start + 1, min_len):
            substr = data[min_len_idx][start:end]
            # Check if this is a substring of all sequences.
            flag = True
            for seq in data:
                if substr not in seq:
                    flag = False
                    break
            # If it is, compare with the longest substring.
            if flag:
                if len(substr) > len(longest_substr):
                    longest_substr = substr
    print(longest_substr)
    return


if __name__ == "__main__":
    main()

