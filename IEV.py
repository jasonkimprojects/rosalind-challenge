# Copyright 2019 Jason Kim. All rights reserved.
# IEV.py
# My solution to IEV of the Rosalind Project.
# Jason Kim
# 7/24/2019


def main():
    # Let genotypes be identified by the following:
    # AA Homozygous Dominant = d
    # Aa Heterozygous = h
    # aa Homozygous Recessive = r
    # Pair of letters indicates mating e.g. dr, hh
    # Constants for probability of dominant phenotype in offspring.
    pr_dd = 1
    pr_dh = 1
    pr_dr = 1
    pr_hh = 0.75
    pr_hr = 0.5
    pr_rr = 0
    probabilities = [pr_dd, pr_dh, pr_dr, pr_hh, pr_hr, pr_rr]
    # Get number of couples with the corresponding genotypes
    file = open("rosalind_iev.txt", "r")
    params = file.readline().split(' ')
    file.close()
    dd = int(params[0])
    dh = int(params[1])
    dr = int(params[2])
    hh = int(params[3])
    hr = int(params[4])
    rr = int(params[5])
    quantities = [dd, dh, dr, hh, hr, rr]
    # Expected value formula w/ 2 offspring each
    total = 0.0
    for i in range(len(quantities)):
        total += (2 * probabilities[i] * quantities[i])
    print(total)
    return


if __name__ == "__main__":
    main()

