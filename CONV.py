# Copyright 2019 Jason Kim. All rights reserved.
# CONV.py
# My solution to CONV of the Rosalind Project.
# Jason Kim
# 8/4/2019


def main():
    file = open("rosalind_conv.txt", "r")
    # More Python string processing fuckery - parse as list of floats
    s1 = list(map(float, file.readline().strip().split(' ')))
    s2 = list(map(float, file.readline().strip().split(' ')))
    file.close()
    # Make the minkowski difference s1 - s2.
    minkowski_diff = []
    # Hash table to keep track of multiplicities.
    element_mults = {}
    for num1 in s1:
        for num2 in s2:
            # To avoid rounding errors. Rosalind input is also
            # rounded to 5 decimal places.
            elt = round(num1 - num2, 5)
            minkowski_diff.append(elt)
            if elt in element_mults:
                element_mults[elt] += 1
            else:
                element_mults[elt] = 1
    # Search the hash table for largest multiplicity and the element
    # that matches it.
    most_freq_elt = 0.0
    max_multiplicity = 0
    for elt, mult in element_mults.items():
        if mult > max_multiplicity:
            max_multiplicity = mult
            most_freq_elt = elt
    print(max_multiplicity)
    print(abs(most_freq_elt))
    return


if __name__ == "__main__":
    main()

