# Copyright 2019 Jason Kim. All rights reserved.
# REVC.py
# My solution to REVC of the Rosalind Project.
# Jason Kim
# 7/23/2019


def main():
    file = open("rosalind_revc.txt", "r")
    revc = ''
    for char in reversed(file.read()):
        if char == 'A':
            revc += 'T'
        elif char == 'T':
            revc += 'A'
        elif char == 'G':
            revc += 'C'
        elif char == 'C':
            revc += 'G'
    print(revc)


if __name__ == "__main__":
    main()

