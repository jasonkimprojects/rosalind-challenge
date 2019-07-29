# Copyright 2019 Jason Kim. All rights reserved.
# TRAN.py
# My solution to TRAN of the Rosalind Project.
# Jason Kim
# 7/29/2019


def main():
    file = open("rosalind_tran.txt", "r")
    strings = []
    buffer = ''
    for line in file:
        if line[0] == '>':
            if buffer:
                strings.append(buffer)
                buffer = ''
        else:
            buffer += line.replace('\n', '')
    file.close()
    # Append last buffer manually
    strings.append(buffer)
    # Sanity checks
    assert len(strings) == 2
    assert len(strings[0]) == len(strings[1])
    num_transitions = 0
    num_transversions = 0
    purines = ['A', 'G']
    pyrimidines = ['C', 'T']
    # Compare char by char
    first = strings[0]
    second = strings[1]
    for i in range(len(strings[0])):
        if first[i] != second[i]:
            if (first[i] in purines and second[i] in purines) or\
               (first[i] in pyrimidines and second[i] in pyrimidines):
                num_transitions += 1
            else:
                num_transversions += 1
    print(round(num_transitions / num_transversions, 11))
    return


if __name__ == "__main__":
    main()

