# Copyright 2019 Jason Kim. All rights reserved.
# CORR.py
# My solution to CORR of the Rosalind Project.
# Jason Kim
# 7/30/2019


# Returns the reverse complement of a DNA sequence.
def rev_complement(sequence):
    complement_of = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }
    seq_reverse = sequence[::-1]
    revc = ''
    for char in seq_reverse:
        revc += complement_of[char]
    return revc


# Returns the Hamming distance between two DNA sequences.
def hamming_dist(first, second):
    assert len(first) == len(second)
    count = 0
    for i in range(len(first)):
        if first[i] != second[i]:
            count += 1
    return count


def main():
    file = open("rosalind_corr.txt", "r")
    buffer = ''
    # Hash table to store sequences as keys and number of
    # occurrences as values. Does NOT include reverse complements.
    occurrences = {}
    for line in file:
        if line[0] == '>':
            if buffer:
                # Check the sequence and its reverse complement.
                # If either exists, increase value of key in hash table.
                if buffer in occurrences:
                    occurrences[buffer] += 1
                elif rev_complement(buffer) in occurrences:
                    occurrences[rev_complement(buffer)] += 1
                # Else, create a new key-value pair.
                else:
                    occurrences[buffer] = 1
                # Reset buffer after addition.
                buffer = ''
        else:
            buffer += line.replace('\n', '')
    # Must process the last buffer manually.
    file.close()
    if buffer in occurrences:
        occurrences[buffer] += 1
    elif rev_complement(buffer) in occurrences:
        occurrences[rev_complement(buffer)] += 1
    else:
        occurrences[buffer] = 1
    # Separate the CORRECT keys in the dictionary that
    # have a value (# of occurrences) of at least 2
    # into a list of correct sequences.
    correct_seqs = []
    for key in occurrences:
        if occurrences[key] >= 2:
            # Can't pop key yet because it breaks the iterator
            correct_seqs.append(key)
    # Now pop the keys that were copied into occurrences
    for duplicate_key in correct_seqs:
        occurrences.pop(duplicate_key)
    # Save length before adding reverse complements
    old_length = len(correct_seqs)
    # For all the correct sequences, append their reverse
    # complements to correct_seqs
    for i in range(old_length):
        # Because we're appending to the end, the items at
        # earlier indices are preserved.
        correct_seqs.append(rev_complement(correct_seqs[i]))
    # Now traverse over the incorrect sequences in the dictionary.
    for key in occurrences:
        # Compare the Hamming distance of this key with that of
        # all the correct sequences.
        for seq in correct_seqs:
            # Hamming distance is 1 with respect to exactly one
            # correct read, per the specifications.
            if hamming_dist(key, seq) == 1:
                print(key + "->" + seq)
    return


if __name__ == "__main__":
    main()

