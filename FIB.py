# Copyright 2019 Jason Kim. All rights reserved.
# FIB.py
# My solution to FIB of the Rosalind Project.
# Jason Kim
# 7/24/2019


def main():
    file = open("rosalind_fib.txt", "r")
    params = file.read().split(' ')
    months = int(params[0])
    multiplier = int(params[1])
    # Don't need the file anymore
    file.close()
    # Let DP memo consist of the following:
    # [newborns, adults]
    # Row 0 = month 1, and so on.
    # Define base case: 1 newborn pair.
    memo = [[1, 0]]
    i = 0
    # End of DP reached when number of rows = months.
    while i < (months - 1):
        # Number of adults = previous adults + previous newborns
        adults = memo[i][1] + memo[i][0]
        # Number of newborns = previous adults * multiplier
        newborns = memo[i][1] * multiplier
        memo.append([newborns, adults])
        i += 1
    # Answer is the sum of the last row.
    print(memo[i][0] + memo[i][1])
    return


if __name__ == "__main__":
    main()

