# Copyright 2019 Jason Kim. All rights reserved.
# CAT.py
# My solution to CAT of the Rosalind Project.
# Jason Kim
# 7/29/2019

# I attempted to solve this recursively, but realized soon enough
# that it will not be computable within the 5 min time limit that
# Rosalind puts. I credit Charles Determan's approach with a cache
# https://github.com/cdeterman/Rosalind/blob/master/033_CAT/033_CAT.py
# as my inspiration to use a memo combined with a little more computation
# as a tradeoff for less unnecessary memo space.


# Returns a boolean signaling if the input is a valid base pair.
def is_pair(x, y):
    if x == 'A' and y == 'U':
        return True
    elif x == 'U' and y == 'A':
        return True
    elif x == 'G' and y == 'C':
        return True
    elif x == 'C' and y == 'G':
        return True
    else:
        return False


# Returns a boolean signaling if the string has matching pairs.
def matching_pairs(seq):
    augc = [0, 0, 0, 0]
    for char in seq:
        if char == 'A':
            augc[0] += 1
        elif char == 'U':
            augc[1] += 1
        elif char == 'G':
            augc[2] += 1
        elif char == 'C':
            augc[3] += 1
    if augc[0] == augc[1] and augc[2] == augc[3]:
        return True
    else:
        return False


# Returns the number of noncrossing perfect matchings for the
# given sequence, mod 1000000.
def noncrossing_matchings(seq, memo):
    if seq not in memo:
        total = 0
        # More efficient to skip by two because each subsequence
        # must have an even number of bases, anyway.
        for m in range(1, len(seq), 2):
            # Two things to check. Make sure that 0, m is a valid
            # base pair, and make sure that the left subsequence
            # seq[1:m] which is from seq[1] to seq[m-1] has matching
            # pairs. Due to the precondition being that there are as
            # many As as Us and as many Cs as Gcs, if the left sub-
            # sequence has matching pairs then the right subsequence
            # will also have matching pairs.
            if is_pair(seq[0], seq[m]) and\
               matching_pairs(seq[1:m]):
                total += (noncrossing_matchings(seq[1:m], memo) *
                          noncrossing_matchings(seq[m + 1:], memo))
        # Add the result to the memo.
        memo[seq] = total
    return memo[seq]


def main():
    file = open("rosalind_cat.txt", "r")
    seq = ''
    # Inspired by Charles Determan.
    # Memo never contains odd length strings or strings where
    # the As don't match Us or the Cs don't match Gs, which is
    # the difference in my implementation. Those two conditions
    # are checked by my helper functions.
    memo = {
        '': 1,
        'AU': 1,
        'UA': 1,
        'CG': 1,
        'GC': 1,
        'AA': 0,
        'AC': 0,
        'AG': 0,
        'CA': 0,
        'CC': 0,
        'CU': 0,
        'GA': 0,
        'GG': 0,
        'GU': 0,
        'UC': 0,
        'UG': 0,
        'UU': 0
    }
    for line in file:
        if line[0] != '>':
            seq += line.replace('\n', '')
    file.close()
    print(noncrossing_matchings(seq, memo) % 1000000)
    return


if __name__ == "__main__":
    main()

