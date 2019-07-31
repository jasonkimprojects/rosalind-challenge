# Copyright 2019 Jason Kim. All rights reserved.
# LCSQ.py
# My solution to LCSQ of the Rosalind Project.
# Jason Kim
# 7/30/2019
# Save the last character of the common subsequence.


def main():
    file = open("rosalind_lcsq.txt", "r")
    strings = []
    buffer = ''
    for line in file:
        if line[0] == '>':
            if buffer:
                strings.append(buffer)
                buffer = ''
        else:
            buffer += line.replace('\n', '')
    strings.append(buffer)
    file.close()
    # Append to longest common subsequence whenever matching
    # last character is found.
    first = strings[0]
    second = strings[1]
    # If len(first) = m and len(second) = n, the memo for DP
    # is an (m+1) x (n+1) matrix to account for the zeroth char.
    # memo holds the longest common
    # subsequence ITSELF of the substrings first[:a] and second[:b].
    memo = [['' for i in range(len(second) + 1)] for j in range(len(first) + 1)]
    # Build the solution bottom-up.
    for x in range(len(first) + 1):
        for y in range(len(second) + 1):
            # If either is zero, then there is no LCS. Length is zero.
            if x == 0 or y == 0:
                memo[x][y] = ''
            # If the last chars match, then the LCS is one longer than the
            # LCS of the two substrings minus their last chars.
            elif first[x - 1] == second[y - 1]:
                memo[x][y] = memo[x - 1][y - 1] + first[x - 1]
            else:
                # If the last chars don't match, the LCS is whatever is
                # the greater out of LCS(first string minus last char) or
                # LCS(second string minus last char).
                if len(memo[x - 1][y]) >= len(memo[x][y - 1]):
                    memo[x][y] = memo[x - 1][y]
                else:
                    memo[x][y] = memo[x][y - 1]
    print(memo[len(first)][len(second)])
    return


if __name__ == "__main__":
    main()

