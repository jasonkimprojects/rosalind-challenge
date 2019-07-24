# Copyright 2019 Jason Kim. All rights reserved.
# RNA.py
# My solution to RNA of the Rosalind Project.
# Jason Kim
# 7/23/2019


def main():
    file = open("rosalind_rna.txt", "r")
    print(file.read().replace('T', 'U'))
    file.close()
    return


if __name__ == "__main__":
    main()

