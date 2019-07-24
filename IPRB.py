# Copyright 2019 Jason Kim. All rights reserved.
# IPRB.py
# My solution to IPRB of the Rosalind Project.
# Jason Kim
# 7/24/2019
import math


# Helper function for calculating binomial coefficient
def ncr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


def main():
    # Constants for probability in simple Mendelian inheritance
    # HD = homozygous dominant
    # HZ = heterozygous
    # HR = homozygous recessive
    HD_HD = 1
    HZ_HZ = 0.75
    HR_HR = 0
    HD_HZ = 1
    HZ_HR = 0.5
    HD_HR = 1
    # Parse file to get # of individuals per genotype
    file = open("rosalind_iprb.txt", "r")
    params = file.readline().split(' ')
    num_HD = int(params[0])
    num_HZ = int(params[1])
    num_HR = int(params[2])
    file.close()
    # Compute nCr(total # of individuals, 2)
    total_pairs = ncr(num_HD + num_HZ + num_HR, 2)
    # Then calculate probability of each genotype pair to mate
    pr_HD_HD = ncr(num_HD, 2) / total_pairs
    pr_HZ_HZ = ncr(num_HZ, 2) / total_pairs
    pr_HR_HR = ncr(num_HR, 2) / total_pairs
    pr_HD_HZ = (num_HD * num_HZ) / total_pairs
    pr_HZ_HR = (num_HZ * num_HR) / total_pairs
    pr_HD_HR = (num_HD * num_HR) / total_pairs
    # Compute Pr(genotype pair mating) *
    # Pr(offspring of that pair having A) and sum
    total = 0.0
    total += (pr_HD_HD * HD_HD)
    total += (pr_HZ_HZ * HZ_HZ)
    total += (pr_HR_HR * HR_HR)
    total += (pr_HD_HZ * HD_HZ)
    total += (pr_HZ_HR * HZ_HR)
    total += (pr_HD_HR * HD_HR)
    print(round(total, 5))
    return


if __name__ == "__main__":
    main()

