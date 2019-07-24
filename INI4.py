# Copyright 2019 Jason Kim. All rights reserved.
# INI4.py
# My solution to INI4 of the Rosalind Project.
# Jason Kim
# 7/23/2019


def main():
    file = open("rosalind_ini4.txt", "r")
    params = file.read().split(' ')
    start = int(params[0])
    end = int(params[1]) + 1
    total = 0
    for num in range(start, end):
        if num % 2 == 1:
            total += num
    print(total)
    return


if __name__ == "__main__":
    main()

