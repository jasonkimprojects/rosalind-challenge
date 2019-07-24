# Copyright 2019 Jason Kim. All rights reserved.
# INI6.py
# My solution to INI6 of the Rosalind Project.
# Jason Kim
# 7/23/2019


def main():
    file = open("rosalind_ini6.txt", "r")
    words = file.read().split(' ')
    dic = {}
    for word in words:
        word = word.strip('\n')
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    for key, value in dic.items():
        print(key, end=' ')
        print(value)
    file.close()
    return


if __name__ == "__main__":
    main()

