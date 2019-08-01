# Copyright 2019 Jason Kim. All rights reserved.
# SSET.py
# My solution to SSET of the Rosalind Project.
# Jason Kim
# 8/1/2019


def main():
    file = open("rosalind_sset.txt", "r")
    n = int(file.readline().replace('\n', ''))
    file.close()
    # This problem is asking the total number of subsets
    # of a set with cardinality n.
    # In other words, the answer is the cardinality of the
    # power set of a set with cardinality n,
    # which has a formula: 2^n.
    # EECS 203 made this a lot easier.
    print(2**n % 1000000)
    return


if __name__ == "__main__":
    main()

