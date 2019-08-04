# Copyright 2019 Jason Kim. All rights reserved.
# SCSP.py
# My solution to SCSP of the Rosalind Project.
# Jason Kim
# 8/3/2019


def main():
    file = open("rosalind_scsp.txt", "r")
    first = file.readline().strip()
    second = file.readline().strip()
    file.close()
    # Build a memo for dynamic programming. The memo will
    # store the shortest common supersequences.
    # memo[i][j] holds the length of the
    # shortest common supersequence for
    # first[:i] and second[:j] in Python format.
    memo = [[0 for a in range(len(second) + 1)]
            for b in range(len(first) + 1)]
    # Then build the solution bottom-up.
    for i in range(len(first) + 1):
        for j in range(len(second) + 1):
            # Base cases: if either substring is empty,
            # then the shortest common supersequence is the
            # other substring.
            if i == 0:
                memo[i][j] = j
            elif j == 0:
                memo[i][j] = i
            # If their last characters match, then that
            # is part of the shortest common supersequence. Include it.
            elif first[i - 1] == second[j - 1]:
                memo[i][j] = memo[i - 1][j - 1] + 1
            else:
                # If they don't, find the shortest SCS among
                # memo[i-1][j] (no last char of first) and
                # memo[i][j-1] (no last char of second).
                memo[i][j] = min(memo[i - 1][j], memo[i][j - 1]) + 1
    # Now we have the length of the shortest common supersequence.
    # To find it, we must trace how the length was formed in reverse.
    scs_idx = memo[len(first)][len(second)]
    # scs will store the chars of the shortest common supersequence as a list.
    scs = ['' for k in range(scs_idx)]
    # Keep track of the indices of both strings, relative to the memo.
    first_idx = len(first)
    second_idx = len(second)
    while first_idx > 0 and second_idx > 0:
        # If the last characters are the same, then the
        # current character is inclued in the shortest common supersequence.
        if first[first_idx - 1] == second[second_idx - 1]:
            scs[scs_idx - 1] = first[first_idx - 1]
            first_idx -= 1
            second_idx -= 1
            scs_idx -= 1
        # Otherwise, find the shortest SCS among (no last char of first)
        # and (no last char of second).
        elif memo[first_idx - 1][second_idx] <\
                memo[first_idx][second_idx - 1]:
            scs[scs_idx - 1] = first[first_idx - 1]
            # Only decrement the first index and the scs index
            first_idx -= 1
            scs_idx -= 1
        else:
            scs[scs_idx - 1] = second[second_idx - 1]
            # Only decrement the second index and the scs index
            second_idx -= 1
            scs_idx -= 1
    # Then add the remaining chars of first.
    while first_idx > 0:
        scs[scs_idx - 1] = first[first_idx - 1]
        first_idx -= 1
        scs_idx -= 1
    # Then add the remaining chars of second.
    while second_idx > 0:
        scs[scs_idx - 1] = second[second_idx - 1]
        second_idx -= 1
        scs_idx -= 1
    # Print element-by-element.
    for char in scs:
        print(char, end='')
    return


if __name__ == "__main__":
    main()

