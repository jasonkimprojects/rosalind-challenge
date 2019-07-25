# Copyright 2019 Jason Kim. All rights reserved.
# SPLC.py
# My solution to SPLC of the Rosalind Project.
# Jason Kim
# 7/25/2019


def main():
    # Single letter codon table.
    # Copied from my PROT.py.
    table = {
        "UUU": 'F',
        "UUC": 'F',
        "UUA": 'L',
        "UUG": 'L',
        "UCU": 'S',
        "UCC": 'S',
        "UCA": 'S',
        "UCG": 'S',
        "UAU": 'Y',
        "UAC": 'Y',
        "UAA": "STOP",
        "UAG": "STOP",
        "UGU": 'C',
        "UGC": 'C',
        "UGA": "STOP",
        "UGG": 'W',
        "CUU": 'L',
        "CUC": 'L',
        "CUA": 'L',
        "CUG": 'L',
        "CCU": 'P',
        "CCC": 'P',
        "CCA": 'P',
        "CCG": 'P',
        "CAU": 'H',
        "CAC": 'H',
        "CAA": 'Q',
        "CAG": 'Q',
        "CGU": 'R',
        "CGC": 'R',
        "CGA": 'R',
        "CGG": 'R',
        "AUU": 'I',
        "AUC": 'I',
        "AUA": 'I',
        "AUG": 'M',
        "ACU": 'T',
        "ACC": 'T',
        "ACA": 'T',
        "ACG": 'T',
        "AAU": 'N',
        "AAC": 'N',
        "AAA": 'K',
        "AAG": 'K',
        "AGU": 'S',
        "AGC": 'S',
        "AGA": 'R',
        "AGG": 'R',
        "GUU": 'V',
        "GUC": 'V',
        "GUA": 'V',
        "GUG": 'V',
        "GCU": 'A',
        "GCC": 'A',
        "GCA": 'A',
        "GCG": 'A',
        "GAU": 'D',
        "GAC": 'D',
        "GAA": 'E',
        "GAG": 'E',
        "GGU": 'G',
        "GGC": 'G',
        "GGA": 'G',
        "GGG": 'G'
    }
    file = open("rosalind_splc.txt", "r")
    lines = file.readlines()
    file.close()
    introns = []
    buffer = ''
    for line in lines:
        if line[0] == '>':
            if buffer:
                # Add when buffer is not empty
                introns.append(buffer)
                buffer = ''
        else:
            buffer += line.replace('\n', '')
    # Must append last buffer manually
    introns.append(buffer)
    # Extract the sequence from the list
    seq = introns.pop(0)
    # Splicing step
    for intron in introns:
        while intron in seq:
            start_idx = seq.find(intron)
            prefix = seq[:start_idx]
            suffix = seq[start_idx + len(intron):]
            seq = prefix + suffix
    # Transcription: Replace Thymine with Uracil
    seq = seq.replace('T', 'U')
    # Translation
    protein = ''
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i + 3]
        amino_acid = table[codon]
        if amino_acid == 'STOP':
            break
        else:
            protein += amino_acid
    print(protein)
    return


if __name__ == "__main__":
    main()

