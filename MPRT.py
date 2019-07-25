# Copyright 2019 Jason Kim. All rights reserved.
# MPRT.py
# My solution to MPRT of the Rosalind Project.
# Jason Kim
# 7/25/2019
import urllib.request


def main():
    file = open("rosalind_mprt.txt", "r")
    params = file.readlines()
    file.close()
    # Get rid of newline characters
    for i in range(len(params)):
        params[i] = params[i].replace('\n', '')
    # Request the FASTA file and read it for each ID
    for j in range(len(params)):
        prefix = "https://www.uniprot.org/uniprot/"
        suffix = ".fasta"
        url = prefix + params[j] + suffix
        fasta = urllib.request.urlopen(url).read()
        # Decode bytes to string
        fasta = fasta.decode("utf-8")
        # Get rid of header
        fasta = fasta[fasta.find('\n') + 1:]
        # Get rid of subsequent newlines
        fasta = fasta.replace('\n', '')
        # Replace entry with [ID, sequence] pair
        params[j] = [params[j], fasta]
    # For each entry, scan for the N-glycosylation motif.
    for k in range(len(params)):
        sequence = params[k][1]
        indices = []
        # Scan every set of 4 chars till the end.
        # The motif is N {P} [ST] {P}
        for idx in range(len(sequence) - 4):
            flag1 = sequence[idx] == 'N'
            flag2 = sequence[idx + 1] != 'P'
            flag3 = sequence[idx + 2] == 'S' or sequence[idx + 2] == 'T'
            flag4 = sequence[idx + 3] != 'P'
            # Check if all four flags are true.
            if flag1 and flag2 and flag3 and flag4:
                # Rosalind wants 1-based indexing.
                indices.append(idx + 1)
        # Replace the sequence with indices.
        params[k][1] = indices
    # Reiterate over each line, print data if indices is not empty.
    for item in params:
        # If indices is not empty, this will evaluate to True.
        if item[1]:
            print(item[0])
            for num in item[1]:
                print(num, end=' ')
            # Newline before next ID
            print()
    return


if __name__ == "__main__":
    main()

