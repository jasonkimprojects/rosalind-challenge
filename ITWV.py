# Copyright 2019 Jason Kim. All rights reserved.
# ITWV.py
# My solution to ITWV of the Rosalind Project.
# Jason Kim
# 8/6/2019


# Helper function to count the number of A/T/G/C that
# the string contains. Returns a string "ATGC" where
# each letter is a number marking the occurrences of that letter.
def count_bases(string):
    arr = [0 for i in range(4)]
    for char in string:
        if char == 'A':
            arr[0] += 1
        elif char == 'T':
            arr[1] += 1
        elif char == 'G':
            arr[2] += 1
        elif char == 'C':
            arr[3] += 1
    result = ''
    for num in arr:
        result += str(num)
    return result


# Searches a sliding window of n chars, where n is the sum of
# occurrences of A,T,G,C. If the count of that substring in string
# is equal to the one passed, it returns the substring.
# May return multiple substrings - so a set is returned.
def potential_substr(string, count):
    length = 0
    matches = set()
    for char in count:
        length += int(char)
    for i in range(len(string) - length + 1):
        substr = string[i:length + i]
        if count_bases(substr) == count:
            matches.add(substr)
    return matches


# Returns whether the two substrings can be interleaved
# inside the larger string.
def interleaved(small1, small2, large):
    # DP memo. memo[i][j] is true if large[:i + j] is an
    # interleaving of small1[:i] and small2[:j]. Init to false.
    memo = [[False for i in range(len(small2) + 1)] for j in range(len(small1) + 1)]
    # Iterate through all characters of small1 and small2.
    for one in range(len(small1) + 1):
        for two in range(len(small2) + 1):
            # Base case: an empty string interleaves two empty strings.
            if one == 0 and two == 0:
                memo[one][two] = True
            # If small1 is empty, just need to check if small2 and
            # large have the same last character.
            elif one == 0 and small2[two - 1] == large[two - 1]:
                # Then the result depends on small2 minus this last
                # char, and this result is precomputed.
                memo[one][two] = memo[one][two - 1]
            # Likewise, if small2 is empty we just need to check if
            # small1 and large have matching last chars
            elif two == 0 and small1[one - 1] == large[one - 1]:
                memo[one][two] = memo[one - 1][two]
            # If the last chars of small1, small2, and large are all
            # identical, then whether they can interleave depends if
            # either small1 minus last char and small2, or:
            # small1 and small2 minus last char can be interleaved.
            elif small1[one - 1] == large[one + two - 1] and\
                    small2[two - 1] == large[one + two - 1]:
                memo[one][two] = memo[one - 1][two] or\
                                 memo[one][two - 1]
            # If the last chars of small1 and large match but not
            # with small2, then whether they can interleave depends on
            # if small1 minus the last char and small2 can interleave.
            elif small1[one - 1] == large[one + two - 1] and\
                    small2[two - 1] != large[one + two - 1]:
                memo[one][two] = memo[one - 1][two]
            # If the last chars of small2 and large match but not
            # with small1, then likewise whether they can interleave
            # depends on small2 minus last char.
            elif small1[one - 1] != large[one + two - 1] and\
                    small2[two - 1] == large[one + two - 1]:
                memo[one][two] = memo[one][two - 1]
    # Then the interleaving of the entire large, small1, and small2
    # strings is computed at the bottom right of this memo.
    return memo[len(small1)][len(small2)]


def main():
    file = open("rosalind_itwv.txt", "r")
    patterns = file.readlines()
    file.close()
    for i in range(len(patterns)):
        patterns[i] = patterns[i].strip()
    dna_string = patterns.pop(0)
    matrix = [[-1 for j in range(len(patterns))] for k in range(len(patterns))]
    # Now iterate over the patterns to create the matrix.
    # A more optimized algorithm would be to compute just the upper triangle
    # of the matrix and then copy the values over to the lower triangle.
    for row in range(len(patterns)):
        for col in range(len(patterns)):
            pattern1 = patterns[row]
            pattern2 = patterns[col]
            count = count_bases(pattern1 + pattern2)
            # Check if an interweaving is possible.
            interleave = potential_substr(dna_string, count)
            # If empty, matrix element is automatically zero.
            # Don't need to proceed for this iteration.
            if len(interleave) == 0:
                matrix[row][col] = 0
                continue
            # Then for each substring in interleave, check if an
            # interweaving is possible.
            for substr in interleave:
                matrix[row][col] = 0
                if interleaved(pattern1, pattern2, substr):
                    matrix[row][col] = 1
                    # If possible, nothing else to do.
                    break
    # Print matrix in Rosalind's format.
    for row in matrix:
        for num in row:
            print(num, end=' ')
        print()
    return


if __name__ == "__main__":
    main()

