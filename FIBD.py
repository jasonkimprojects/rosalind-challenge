# Copyright 2019 Jason Kim. All rights reserved.
# FIBD.py
# My solution to FIBD of the Rosalind Project.
# Jason Kim
# 7/24/2019


def main():
    # DP Problem, but recursion depth of only 1.
    # A memo with just the previous month recored would suffice,
    # but I'm using the entire memo to show memoization.
    file = open("rosalind_fibd.txt", "r")
    params = file.readline().split(' ')
    months = int(params[0])
    max_age = int(params[1])
    # 2D memo, zero initialized
    memo = [[0 for i in range(max_age)] for j in range(months)]
    # Base case: month 1 starts with 1 pair of 1 month old rabbits
    memo[0][0] = 1
    # DP step : build bottom-up
    for n in range(1, months):
        # Make the rabbits age, except for the ones that die
        memo[n][1:max_age] = memo[n-1][:max_age - 1]
        # Compute number of 1 month olds
        memo[n][0] = sum(memo[n-1][1:])
    # Reverse indices: -1 points to end of list
    print(sum(memo[-1]))
    file.close()
    return


if __name__ == "__main__":
    main()

