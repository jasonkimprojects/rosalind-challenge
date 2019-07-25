# Copyright 2019 Jason Kim. All rights reserved.
# REVP.py
# My solution to REVP of the Rosalind Project.
# Jason Kim
# 7/25/2019


def main():
    file = open("rosalind_revp.txt", "r")
    lines = file.readlines()
    file.close()
    # Read forward sequence by parsing the file
    dna_fwd = ''
    for line in lines:
        if line[0] != '>':
            dna_fwd += line.replace('\n', '')
    # Derive its complement.
    dna_c = ''
    for char in dna_fwd:
        if char == 'A':
            dna_c += 'T'
        elif char == 'T':
            dna_c += 'A'
        elif char == 'G':
            dna_c += 'C'
        elif char == 'C':
            dna_c += 'G'
    # Sanity check
    assert len(dna_fwd) == len(dna_c)
    # Loop for all substrings
    for start in range(len(dna_fwd)):
        for end in range(start + 1, len(dna_fwd) + 1):
            # Can go 'past the end' because end index for
            # substring is exclusive.
            fwd_substr = dna_fwd[start:end]
            revc_substr = dna_c[start:end]
            # Reverse it for comparison.
            revc_substr = revc_substr[::-1]
            # Check length
            flag1 = len(fwd_substr) >= 4
            flag2 = len(fwd_substr) <= 12
            # Then check if palindrome
            if flag1 and flag2 and fwd_substr == revc_substr:
                # Rosalind wants 1-based indexing
                print(start + 1, end=' ')
                print(len(fwd_substr))
    return


if __name__ == "__main__":
    main()

