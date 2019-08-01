# Copyright 2019 Jason Kim. All rights reserved.
# EDIT.py
# My solution to EDIT of the Rosalind Project.
# Jason Kim
# 8/1/2019


def main():
    file = open("rosalind_edit.txt", "r")
    data = file.readlines()
    file.close()
    # Buffer for FASTA string
    buffer = ''
    strings = []
    # data[0] is always a FASTA header
    for i in range(1, len(data)):
        # If we encounter a header
        if data[i][0] == '>':
            strings.append(buffer)
            buffer = ''
        # If we reach the end
        elif i == len(data) - 1:
            buffer += data[i].strip()
            strings.append(buffer)
        else:
            buffer += data[i].strip()
    # References for easier readability
    str1 = strings[0]
    str2 = strings[1]
    # Create a memo for DP, with dimensions len(str1) + 1 by
    # len(str2) + 1, to accommodate for the case of length zero.
    # memo[i][j] holds the minimum edit distance for the substrings
    # str1[:i] and str2[:j].
    memo = [[-1 for a in range(len(str2) + 1)] for b in range(len(str1) + 1)]
    # Now iterate over the entire memo, filling it up.
    for x in range(len(memo)):
        for y in range(len(memo[0])):
            # Base case 1. If x is zero, str1 is empty.
            # Then the min edit distance is the length of str2[:y]
            # which is y (since y chars must be inserted into str1).
            if x == 0:
                memo[x][y] = y
            # Base case 2. If y is zero, str2 is empty.
            # Then the min edit distance is the length of str1[:x]
            # which is x (since x chars must be inserted into str2).
            elif y == 0:
                memo[x][y] = x
            # If the last chars of str1[:x] and str2[:y] i.e.
            # str1[x-1] and str2[y-1] are equal, then there is no
            # difference in edit distance from the two substrings
            # minus their last characters, which would be str1[:x-1]
            # and str2[:y-1].
            elif str1[x - 1] == str2[y - 1]:
                memo[x][y] = memo[x - 1][y - 1]
            # Finally, if both substrings are not empty and do not have
            # the same last character:
            else:
                # This is probably the best explanation one can make
                # about why the dynamic programming memo works.
                # Three manipulations we can do to str1:
                # Change the last char of str1 to the last char of str2.
                # Then the cost is 1 for the replacement +
                # cost of str1[:x-1] vs str2[:y-1] because now their last
                # chars are equal. Don't need to compare them.
                change = memo[x - 1][y - 1] + 1
                # Insert the last char of str2 to the end of str1.
                # Then the cost is 1 for the insertion +
                # cost of str1[:x] vs str2[:y-1] because now their last
                # chars are equal, don't need to compare them, but str1
                # must be compared to x because the added char is x+1.
                insert = memo[x][y - 1] + 1
                # Remove the last char of str2. Then the cost is 1
                # for the deletion + cost of str1[:x-1] vs str2[:y]
                # because str1[x] is now out of the question, it
                # was deleted.
                delete = memo[x - 1][y] + 1
                # Now choose the operation with smallest distance.
                memo[x][y] = min(change, insert, delete)
    # Then the cost of mutating str1 into str2 is at
    # memo[len(str1)][len(str2)].
    print(memo[len(str1)][len(str2)])
    return


if __name__ == "__main__":
    main()

