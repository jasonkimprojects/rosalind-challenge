# Copyright 2019 Jason Kim. All rights reserved.
# INI5.py
# My solution to INI5 of the Rosalind Project.
# Jason Kim
# 7/23/2019


def main():
    file_in = open("rosalind_ini5.txt", "r")
    file_out = open("rosalind_ini5_out.txt", "w+")
    count = 1
    for line in file_in:
        if count % 2 == 0:
            file_out.write(line)
        count += 1
    file_in.close()
    file_out.close()
    return


if __name__ == "__main__":
    main()

