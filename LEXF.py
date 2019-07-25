# Copyright 2019 Jason Kim. All rights reserved.
# LEXF.py
# My solution to LEXF of the Rosalind Project.
# Jason Kim
# 7/25/2019


# Recursive helper function for listing permutations
# of set length in the order that elements are listed
# in alphabet.
def permutation(alphabet, length, substr):
    # Base case. One letter short of set length, so
    # just append one more letter in alphabet order.
    if len(substr) == length - 1:
        for char in alphabet:
            perm = substr + char
            print(perm)
    else:
        for char in alphabet:
            # Append char in alphabet order to the current substring
            # and make a recursive call for DFS.
            permutation(alphabet, length, substr + char)


def main():
    file = open("rosalind_lexf.txt", "r")
    # Get rid of newline, then split by space
    alphabet = file.readline().replace('\n', '')
    alphabet = alphabet.split(' ')
    length = int(file.readline())
    file.close()
    permutation(alphabet, length, '')
    return


if __name__ == "__main__":
    main()

