# Copyright 2019 Jason Kim. All rights reserved.
# INI2.py
# My solution to INI2 of the Rosalind Project.
# Jason Kim
# 7/23/2019


def main():
    file = open("rosalind_ini2.txt", "r")
    nums = file.read().split(' ')
    leg_a = int(nums[0])
    leg_b = int(nums[1])
    print(leg_a**2 + leg_b**2)
    file.close()
    return


if __name__ == "__main__":
    main()

