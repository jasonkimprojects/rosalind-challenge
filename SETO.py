# Copyright 2019 Jason Kim. All rights reserved.
# SETO.py
# My solution to SETO of the Rosalind Project.
# Jason Kim
# 8/4/2019


def main():
    file = open("rosalind_seto.txt", "r")
    n = int(file.readline().strip())
    # Python string processing fuckery.
    # strip removes {, }, newline
    # split makes the numbers into a list of strings by delimiting ", "
    # map casts each element into int, and then set casts
    # map object to class set.
    subset1 = set(map(int, file.readline().strip("{}\n").split(", ")))
    subset2 = set(map(int, file.readline().strip("{}\n").split(", ")))
    file.close()
    # Print A union B
    # Fortunately, Python has built-in set operators.
    print(subset1 | subset2)
    # Print A intersection B
    print(subset1 & subset2)
    # Print A minus B
    print(subset1 - subset2)
    # Print B minus A
    print(subset2 - subset1)
    # Create the universal set from numbers 1 to n, inclusive.
    universe = {i for i in range(1, n + 1)}
    # Print A complement
    print(universe - subset1)
    # Print B complement
    print(universe - subset2)
    return


if __name__ == "__main__":
    main()

