# Copyright 2019 Jason Kim. All rights reserved.
# MOTZ.py
# My solution to MOTZ of the Rosalind Project.
# Jason Kim
# 8/1/2019


# A lot of code for this problem was taken from my CAT.py.


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


# Returns the number of noncrossing matchings (not necessarily perfect)
# for the given sequence.
def noncrossing_matchings(seq, memo):
    if seq not in memo:
        # If seq[0] is not involved in a matching, there are
        # noncrossing_matchings(seq[1:], memo) ways to match
        # the remaining nodes.
        total = noncrossing_matchings(seq[1:], memo)
        # IF seq[0] is involved in a matching:
        # Here we can't skip by 2s because each left/right half
        # of a matching CAN have an odd number of bases.
        for m in range(1, len(seq)):
            # First check if they constitute a valid base pair.
            if is_pair(seq[0], seq[m]):
                total += (noncrossing_matchings(seq[1:m], memo) *
                          noncrossing_matchings(seq[m + 1:], memo))
        # Add the result to the memo.
        memo[seq] = total
    return memo[seq]


def main():
    file = open("rosalind_motz.txt", "r")
    seq = ''
    for line in file:
        if line[0] != '>':
            seq += line.strip()
    file.close()
    # Base cases - sequences of length 0 or 1 have ONE matching
    memo = {
        '': 1,
        'A': 1,
        'U': 1,
        'C': 1,
        'G': 1
    }
    print(noncrossing_matchings(seq, memo) % 1000000)
    return


if __name__ == "__main__":
    main()

