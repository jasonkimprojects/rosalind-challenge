# Copyright 2019 Jason Kim. All rights reserved.
# SUBS.py
# My solution to SUBS of the Rosalind Project.
# Jason Kim
# 7/24/2019


def main():
    file = open("rosalind_subs.txt", "r")
    long = file.readline().replace('\n', '')
    short = file.readline().replace('\n', '')
    # Check that short is no longer than long
    assert len(short) <= len(long)
    # Finding all occurrences is O(long) anyway with regex
    file.close()
    for i in range(len(long) - len(short)):
        if long[i:i + len(short)] == short:
            # Rosalind wants 1-based indexing
            print(i + 1, end=' ')
    return


if __name__ == "__main__":
    main()

