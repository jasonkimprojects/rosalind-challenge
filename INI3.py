# Copyright 2019 Jason Kim. All rights reserved.
# INI3.py
# My solution to INI3 of the Rosalind Project.
# Jason Kim
# 7/23/2019


def main():
    file = open("rosalind_ini3.txt", "r")
    contents = file.readlines()
    msg = contents[0]
    indices = contents[1].split(' ')
    start_first = int(indices[0])
    end_first = int(indices[1]) + 1
    start_second = int(indices[2])
    end_second = int(indices[3]) + 1
    print(msg[start_first:end_first] + ' ' + msg[start_second:end_second])
    return


if __name__ == "__main__":
    main()

