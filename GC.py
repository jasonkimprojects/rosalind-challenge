# Copyright 2019 Jason Kim. All rights reserved.
# GC.py
# My solution to GC of the Rosalind Project.
# Jason Kim
# 7/24/2019


def main():
    file = open("rosalind_gc.txt", "r")
    lines = file.readlines()
    hashtable = {}
    # Parse lines into dictionary.
    name = ''
    sequence = ''
    for line in lines:
        # Get rid of carriage returns.
        line = line.replace('\n', '')
        if line[0] == '>':
            if name != '':
                # Add all previous info when a new entry is detected.
                hashtable[name] = sequence
            # Omit the > from the name when storing it.
            name = line[1:]
            sequence = ''
        else:
            sequence += line
    # Add the last pair to the hash table.
    # Must be done explicitly because there is no > after the last pair.
    hashtable[name] = sequence
    # Then calculate GC-content for each entry, keeping track of the maximum.
    max_name = ""
    max_gc = 0.0
    for name, sequence in hashtable.items():
        gc_count = 0
        for char in sequence:
            if char == 'G' or char == 'C':
                gc_count += 1
        # Since we don't need the sequence anymore, replace it with GC-percentage.
        percentage = gc_count / len(sequence) * 100
        hashtable[name] = percentage
        # Check if the GC-content is a new maximum.
        if percentage > max_gc:
            max_gc = percentage
            max_name = name
    print(max_name)
    print(round(max_gc, 6))
    file.close()
    return


if __name__ == "__main__":
    main()

