# Copyright 2019 Jason Kim. All rights reserved.
# CONS.py
# My solution to CONS of the Rosalind Project.
# Jason Kim
# 7/24/2019


def main():
    buffer = ''
    sequences = []
    file = open("rosalind_cons.txt", "r")
    for line in file:
        # Ignore sequence names
        if line[0] == '>':
            if buffer != '':
                sequences.append(buffer)
                buffer = ''
            continue
        else:
            # Get rid of carriage returns
            line = line.replace('\n', '')
            buffer += line
    # Add the last buffer to the list.
    sequences.append(buffer)
    # Consensus matrix: cols are each nucleotide position,
    # rows are A, C, G, T.
    consensus = [[0 for i in range(len(sequences[0]))] for j in range(4)]
    # Parse each sequence, nucleotide by nucleotide
    for sequence in sequences:
        for k in range(len(sequences[0])):
            if sequence[k] == 'A':
                consensus[0][k] += 1
            elif sequence[k] == 'C':
                consensus[1][k] += 1
            elif sequence[k] == 'G':
                consensus[2][k] += 1
            elif sequence[k] == 'T':
                consensus[3][k] += 1
    # Find max per column to devise consensus sequence.
    cons_str = ''
    for col in range(len(sequences[0])):
        maximum = -1
        max_idx = -1
        for row in range(4):
            if consensus[row][col] > maximum:
                maximum = consensus[row][col]
                max_idx = row
        # Decide which nucleotide to add based on max_idx.
        if max_idx == 0:
            cons_str += 'A'
        elif max_idx == 1:
            cons_str += 'C'
        elif max_idx == 2:
            cons_str += 'G'
        elif max_idx == 3:
            cons_str += 'T'
    print(cons_str)
    print("A: ", end='')
    for num in consensus[0]:
        print(num, end=' ')
    print("\nC: ", end='')
    for num in consensus[1]:
        print(num, end=' ')
    print("\nG: ", end='')
    for num in consensus[2]:
        print(num, end=' ')
    print("\nT: ", end='')
    for num in consensus[3]:
        print(num, end=' ')
    file.close()
    return


if __name__ == "__main__":
    main()

