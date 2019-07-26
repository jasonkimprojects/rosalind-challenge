# Copyright 2019 Jason Kim. All rights reserved.
# LGIS.py
# My solution to LGIS of the Rosalind Project.
# Jason Kim
# 7/26/2019


# Helper function to find the longest increasing subsequence.
def longest_increasing(nums):
    # Memo for Dynamic Programming.
    # lis[i] contains the length of the longest increasing
    # subsequence whose last element is nums[i].
    # Base case: lis[0] must be 1, because the LIS ending
    # at nums[0] is nums[0] itself, and of length 1.
    # For all other indices, lis[1] is at least 1 for the same reason.
    lis = [1 for j in range(len(nums))]
    # Second memo for DP.
    # parent[i] contains the index of the second to last
    # element in the longest increasing subsequence whose
    # last element is nums[i]. If nums[i] is the first
    # element of the LIS (no parent), then parent[i] is -1.
    parent = [-1 for k in range(len(nums))]
    # Then iterate from the second array element to the last.
    for x in range(1, len(nums)):
        # If there is no LIS that can accept nums[x] appended to
        # its end as a larger element, then lis[x] defaults to 1.
        for y in range(x):
            # y is always a smaller index than x.
            # If the last LIS number at the smaller index is smaller
            # than the number at the bigger index and the LIS ending
            # at the smaller index is not smaller than the LIS at the bigger
            # index, then we have found a new LIS.
            if nums[y] < nums[x] and lis[y] >= lis[x]:
                lis[x] = lis[y] + 1
                # Record the old largest number in the LIS in the parent memo.
                parent[x] = y
    # Now find the maximum of lis. lis[x] contains the length of the LIS ending
    # at the number at nums[x], so the maximum of lis is the LIS of the entire array.
    max_lis = 0
    # Also find the index where the maximum of lis occurred, because that points
    # to the last item in the LIS of the entire array.
    max_lis_idx = -1
    for z in range(len(nums)):
        if lis[z] > max_lis:
            max_lis = lis[z]
            max_lis_idx = z
    # Now search backwards like union-find to reconstruct the elements of the LIS.
    # Must loop to find previous element while the parent index is not -1
    # (-1 indicates no previous parent).
    lis_elts = []
    while max_lis_idx != -1:
        lis_elts.append(nums[max_lis_idx])
        # Replace with the parent index to get the next largest number in the LIS.
        max_lis_idx = parent[max_lis_idx]
    # Then reverse lis_elts because it was a backwards search for parent.
    lis_elts.reverse()
    # Now lis_elts contains the proper LIS.
    for w in lis_elts:
        print(w, end=' ')
    print()


# Helper function to find the longest decreasing subsequence.
# Since this is a simple variation of the LIS problem with just
# some inequalities reversed, comments have been left out where redundant.
def longest_decreasing(nums):
    lds = [1 for j in range(len(nums))]
    parent = [-1 for k in range(len(nums))]
    for x in range(1, len(nums)):
        for y in range(x):
            # y is always a smaller index than x.
            # If the last number of the LDS ending at the smaller index is greater
            # than the number at the bigger index and the length of LDS ending
            # at the smaller index is not smaller than the length of LDS at the bigger
            # index, then we have found a new LDS.
            # Therefore, nums[y] > nums[x] instead of < in the LIS function.
            if nums[y] > nums[x] and lds[y] >= lds[x]:
                lds[x] = lds[y] + 1
                parent[x] = y
    max_lds = 0
    max_lds_idx = -1
    for z in range(len(nums)):
        if lds[z] > max_lds:
            max_lds = lds[z]
            max_lds_idx = z
    lds_elts = []
    while max_lds_idx != -1:
        lds_elts.append(nums[max_lds_idx])
        max_lds_idx = parent[max_lds_idx]
    lds_elts.reverse()
    for w in lds_elts:
        print(w, end=' ')
    print()


def main():
    file = open("rosalind_lgis.txt", "r")
    # Don't need the length field, because it's Python.
    file.readline()
    # Just put the sequence into a list
    nums = file.readline().split(' ')
    file.close()
    # Convert to ints
    for i in range(len(nums)):
        nums[i] = nums[i].replace('\n', '')
        nums[i] = int(nums[i])
    # Helper functions for longest increasing and decreasing subsequence.
    longest_increasing(nums)
    longest_decreasing(nums)
    return


if __name__ == "__main__":
    main()

