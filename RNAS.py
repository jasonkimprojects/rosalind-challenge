# Copyright 2019 Jason Kim. All rights reserved.
# RNAS.py
# My solution to RNAS of the Rosalind Project.
# Jason Kim
# 8/7/2019


# A lot of code for this problem was taken from my MOTZ.py.


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
    # WOBBLE - Guanine with Uracil!
    elif x == 'G' and y == 'U':
        return True
    elif x == 'U' and y == 'G':
        return True
    else:
        return False


# Returns the number of valid matchings for the given sequence.
def valid_matchings(seq, memo):
    if seq not in memo:
        # If seq[0] is not involved in a matching, there are
        # valid_matchings(seq[1:], memo) ways to match the
        # remaining nodes.
        total = valid_matchings(seq[1:], memo)
        # If seq[0] is involved in a matching:
        # Here we can't skip by 2s because each left/right half
        # of a matching CAN have an odd number of bases.
        # ADDITIONAL CONSTRAINT: The other nucleotide must be at least
        # 4 base pairs away.
        for m in range(4, len(seq)):
            # First check if they constitue a valid base pair.
            if is_pair(seq[0], seq[m]):
                total += (valid_matchings(seq[1:m], memo) *
                          valid_matchings(seq[m + 1:], memo))
        # Add the result to the memo.
        memo[seq] = total
    return memo[seq]


def main():
    file = open("rosalind_rnas.txt", "r")
    seq = ''
    for line in file:
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
    print(valid_matchings(seq, memo))
    return


if __name__ == "__main__":
    main()

