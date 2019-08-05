# Copyright 2019 Jason Kim. All rights reserved.
# DBRU.py
# My solution to DBRU of the Rosalind Project.
# Jason Kim
# 8/5/2019


# Returns the reverse complement of a sequence
def revc(seq):
    pairs = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }
    result = ''
    for base in seq[::-1]:
        result += pairs[base]
    return result


def main():
    file = open("rosalind_dbru.txt", "r")
    set_s = set()
    for line in file:
        set_s.add(line.strip())
    file.close()
    # Get reverse complements
    set_s_rc = set()
    for item in set_s:
        set_s_rc.add(revc(item))
    # Get their union for de Bruijn graph
    set_union = set_s | set_s_rc
    # Make a set for edges of the de Bruijn graph
    edges = set()
    for item in set_union:
        edges.add((item[:len(item) - 1], item[1:]))
    # Print in format Rosalind wants
    for item in edges:
        output = '(' + item[0] + ", " + item[1] + ')'
        print(output)


if __name__ == "__main__":
    main()

