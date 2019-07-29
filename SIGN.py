# Copyright 2019 Jason Kim. All rights reserved.
# SIGN.py
# My solution to SIGN of the Rosalind Project.
# Jason Kim
# 7/29/2019
import math


def sign_perm(nums, start, end):
    # Print the sequence first
    for num in nums:
        print(num, end=' ')
    print()
    # Base case: if start is past the end, then
    # no recursion to do.
    if start > end:
        return
    else:
        for i in range(start, end + 1):
            # Flip sign at index i
            nums[i] = -1 * nums[i]
            # Recursive call with start at i + 1, because
            # Everything up to index i must stay the same down
            # the call stack
            sign_perm(nums, i + 1, end)
            # Backtrack, undo sign flip at index i
            nums[i] = -1 * nums[i]


def permutation(nums, start, end):
    # Base case - everything has been swapped and
    # sent down the recursion stack
    if start == end:
        # Feed to sign permutation function
        sign_perm(nums, 0, end)
    else:
        for i in range(start, end + 1):
            # Python only - swap without temp var
            nums[start], nums[i] = nums[i], nums[start]
            # Recursive call to next swap stage
            permutation(nums, start + 1, end)
            # Backtrack and restore conditions
            nums[start], nums[i] = nums[i], nums[start]


def main():
    file = open("rosalind_sign.txt", "r")
    n = int(file.readline().replace('\n', ''))
    file.close()
    # The number of signed permutations on n =
    # 2^n possibilities for sign *
    # n! possibilities for permutation itself.
    # Sign and permutation are, trivially, independent.
    # Therefore 2^n * n! signed permutations exist.
    print(2**n * math.factorial(n))
    # Prep for backtracking - list nums from 1 up to n
    nums = [i for i in range(1, n + 1)]
    # Call to backtracking function
    permutation(nums, 0, n-1)
    return


if __name__ == "__main__":
    main()

