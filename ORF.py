# Copyright 2019 Jason Kim. All rights reserved.
# ORF.py
# My solution to ORF of the Rosalind Project.
# Jason Kim
# 7/25/2019
import re


def main():
    # Single letter codon table.
    # Copied from my PROT.py
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
    file = open("rosalind_orf.txt", "r")
    lines = file.readlines()
    file.close()
    # Parse the forward sequence
    dna_fwd = ''
    for line in lines:
        if line[0] != '>':
            dna_fwd += line.replace('\n', '')
    # Get the reverse complement
    # Copied from my REVC.py
    dna_revc = ''
    for char in reversed(dna_fwd):
        if char == 'A':
            dna_revc += 'T'
        elif char == 'T':
            dna_revc += 'A'
        elif char == 'G':
            dna_revc += 'C'
        elif char == 'C':
            dna_revc += 'G'
    # Transcribe fwd and revc. In other words,
    # replace everey occurrence of Thymine with Uracil.
    dna_fwd = dna_fwd.replace('T', 'U')
    dna_revc = dna_revc.replace('T', 'U')
    # Put fwd and revc (now RNA) in a list to
    # eliminate code duplication subsequently
    rna_list = [dna_fwd, dna_revc]
    # List for storing candidate protein strings
    candidates = []
    # Iterate over fwd and revc
    for seq in rna_list:
        # Find all occurrences of AUG (start codon)
        # We love regex
        # Source: https://stackoverflow.com/questions/4664850/how-to-find-all-occurrences-of-a-substring
        augs = [m.start() for m in re.finditer('(?=AUG)', seq)]
        # Then compute the protein strings that
        # result from each start codon.
        for start_idx in augs:
            prot_str = ''
            stopped = False
            # Read triplets starting from index of AUG
            for i in range(start_idx, len(seq) - 3, 3):
                codon = seq[i:i + 3]
                amino_acid = table[codon]
                # Trip the stopped flag
                if amino_acid == 'STOP':
                    stopped = True
                    break
                else:
                    prot_str += amino_acid
            # Must check if there was a stop codon at the end
            if prot_str not in candidates and stopped:
                candidates.append(prot_str)
    # Print line by line
    for prot in candidates:
        print(prot)
    return


if __name__ == "__main__":
    main()

