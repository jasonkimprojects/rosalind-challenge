# Copyright 2019 Jason Kim. All rights reserved.
# GRPH.py
# My solution to GRPH of the Rosalind Project.
# Jason Kim
# 7/24/2019


def main():
    file = open("rosalind_grph.txt", "r")
    data = []
    name = ''
    buffer = ''
    for line in file:
        line = line.replace('\n', '')
        if line[0] == '>':
            # Empty sequences evaluate to false.
            if buffer:
                # Buffer is not empty.
                data.append([name, buffer])
            name = line[1:]
            buffer = ''
        else:
            buffer += line
    # Append the last string manually
    data.append([name, buffer])
    file.close()
    # Change the DNA sequence to [prefix3, suffix3]
    for row in range(len(data)):
        prefix = data[row][1][:3]
        suffix = data[row][1][-3:]
        data[row] = [data[row][0], prefix, suffix]
    # Search suffix-prefix links
    for suf_idx in range(len(data)):
        for pre_idx in range(len(data)):
            if data[suf_idx][2] == data[pre_idx][1] and suf_idx != pre_idx:
                print(data[suf_idx][0], end=' ')
                print(data[pre_idx][0])
    return


if __name__ == "__main__":
    main()

