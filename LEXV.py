# Copyright 2019 Jason Kim. All rights reserved.
# LEXV.py
# My solution to LEXV of the Rosalind Project.
# Jason Kim
# 7/31/2019
import copy
import functools


# Helper method for comparing two strings with a custom alphabet.
# Returns 1 if first > second, -1 if first < second, and 0 if
# first = second lexicographically.
def compare(first, second):
    # Iterate up to the shorter length.
    for idx in range(min(len(first), len(second))):
        if order[first[idx]] > order[second[idx]]:
            return 1
        elif order[first[idx]] < order[second[idx]]:
            return -1
    # If execution reaches this point, the two strings have been equal
    # up to the shorter length. First check if the lengths are equal:
    if len(first) == len(second):
        # Strings are lexicographically equal
        return 0
    elif len(first) > len(second):
        # Since the first string is longer, the second string is a prefix
        # of the first string.
        return 1
    else:
        # Since the second string is longer, the first string is a prefix
        # of the second string.
        return -1


file = open("rosalind_lexv.txt", "r")
alphabet = file.readline().split(' ')
max_len = int(file.readline())
file.close()
# Remove carriage returns from the alphabet
for i in range(len(alphabet)):
    alphabet[i] = alphabet[i].replace('\n', '')
# Make a deep copy of the alphabet to begin with,
# for 1-letter permutations.
permutations = copy.deepcopy(alphabet)
# Generate permutations of the alphabet with length greater than 1
# up to max_len
for j in range(1, max_len):
    # Save old length, since new additions will be appended
    old_len = len(permutations)
    for k in range(old_len):
        # For this iteration, only look at permutations of length j
        # because appending chars to shorter ones leads to duplicates
        if len(permutations[k]) == j:
            # Append each letter in the alphabet.
            for char in alphabet:
                permutations.append(permutations[k] + char)
# Generate a hash table of alphabet to letter position for fast lookup.
order = {}
count = 0
for char in alphabet:
    order[char] = count
    count += 1
# Then preparation for the custom comparator is complete.
# Sort using Python 3's built-in sort and make the key
# the custom comparator.
permutations = sorted(permutations, key=functools.cmp_to_key(compare))
# Print using the format Rosalind wants.
for item in permutations:
    print(item)
