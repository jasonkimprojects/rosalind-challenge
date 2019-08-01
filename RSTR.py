# Copyright 2019 Jason Kim. All rights reserved.
# RSTR.py
# My solution to RSTR of the Rosalind Project.
# Jason Kim
# 8/1/2019


def main():
    file = open("rosalind_rstr.txt", "r")
    data = file.readlines()
    file.close()
    # data[0] consists of n then x.
    data[0] = data[0].replace('\n', '').split(' ')
    num_strings = int(data[0][0])
    gc_content = float(data[0][1])
    sequence = data[1].replace('\n', '')
    # If the GC-content is x, then the probability of
    # G/C appearing is x/2 for each and the probability of
    # A/T appearing is (1-x)/2 for each.
    prob_gc = gc_content / 2.0
    prob_at = (1 - gc_content) / 2.0
    # Since the bases are independent of each other, multiply
    # the probabilities out per base in the sequence to get the
    # probability of getting the sequence.
    prob_seq = 1
    for char in sequence:
        if char == 'G' or char == 'C':
            prob_seq *= prob_gc
        elif char == 'A' or char == 'T':
            prob_seq *= prob_at
    # Then, let the EVENT of obtaining this sequence be a Bernoulli
    # trial, where if you get this sequence by fusing A/C/G/T with the
    # GC-content above then it is a success; all other sequences are
    # failures. Pr(at least 1 string out of N random strings equals s) =
    # 1 - Pr(exactly ZERO strings out of N random strings equals s) due to
    # the complement rule.
    # Due to the complement rule again, Pr(not getting sequence) =
    # 1 - Pr(getting sequence).
    prob_not_seq = 1 - prob_seq
    # Then Pr(exactly 0 strings out of N strings equals s) =
    # Pr(zero successes out of N) = nCr(N,0) p^0 (1-p)^(N-0) =
    # (1-p)^N since nCr(N,0) = 1 always.
    prob_zero_matches = prob_not_seq**num_strings
    # Then subtract this value from 1 to obtain the answer.
    print(round(1 - prob_zero_matches, 3))
    return


if __name__ == "__main__":
    main()

