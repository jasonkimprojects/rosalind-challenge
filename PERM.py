# Copyright 2019 Jason Kim. All rights reserved.
# PERM.py
# My solution to PERM of the Rosalind Project.
# Jason Kim
# 7/25/2019
import math


# Helper function for listing all permutations of
# the list given as nums.
# Uses recursion and backtracking.
def permutations(nums, start, end):
    # Base case - everything has been swapped and
    # sent down the recursion stack
    if start == end:
        for num in nums:
            print(num, end=' ')
        # Newline
        print()
    else:
        # Backtracking step
        for i in range(start, end + 1):
            # Python only - swap without temp var
            nums[start], nums[i] = nums[i], nums[start]
            # Recursion but with start incremented, since
            # nums[start] has been swapped
            permutations(nums, start + 1, end)
            # Backtrack - undo swap
            nums[start], nums[i] = nums[i], nums[start]


def main():
    file = open("rosalind_perm.txt", "r")
    n = int(file.readline())
    file.close()
    # A set of n items has n! possible permutations
    print(math.factorial(n))
    # Make a list of the numerals
    nums = [i for i in range(1, n + 1)]
    # Feed to backtracking function
    permutations(nums, 0, n - 1)
    return


if __name__ == "__main__":
    main()

