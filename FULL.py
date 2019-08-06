# Copyright 2019 Jason Kim. All rights reserved.
# FULL.py
# My solution to FULL of the Rosalind Project.
# Jason Kim
# 8/6/2019


def main():
    # I and L have been consolidated into I in the reverse
    # lookup table due to them having identical mass
    # up to 5 decimal points.
    weight_to_acid = {
        71.03711: 'A',
        103.00919: 'C',
        115.02694: 'D',
        129.04259: 'E',
        147.06841: 'F',
        57.02146: 'G',
        137.05891: 'H',
        113.08406: 'I',
        128.09496: 'K',
        131.04049: 'M',
        114.04293: 'N',
        97.05276: 'P',
        128.05858: 'Q',
        156.10111: 'R',
        87.03203: 'S',
        101.04768: 'T',
        99.06841: 'V',
        186.07931: 'W',
        163.06333: 'Y'
    }
    file = open("rosalind_full.txt", "r")
    data = []
    for line in file:
        data.append(float(line.strip()))
    file.close()
    # Record 2n + 3 before popping out parent mass.
    num_lines = len(data)
    # Then perform algebra to get n.
    n = (num_lines - 3) // 2
    parent_mass = data.pop(0)
    # After popping parent, sort ions into complement pairs.
    data.sort()
    pairs = []
    # Ion weights are already sorted and the precondition is that
    # the complement exists for every ion, so we only need to run
    # the outer loop for number of ions / 2.
    for i in range(len(data) // 2):
        # Extra step, but double checking that the complement exists.
        for j in range(len(data)):
            if round(data[i] + data[j], 5) == round(parent_mass, 5):
                pairs.append((data[i], data[j]))
    # Now build the protein string of length n.
    index = 0
    protein = ''
    while index < n:
        # Find an amino acid that is the most accurate
        most_accurate = None
        for key in weight_to_acid:
            # First search from what we assume is the same type
            # of ion, whether it is a b-ion or a y-ion. They would
            # be on the same column for two pairs.
            if round(key, 5) == round(pairs[index + 1][0] - pairs[index][0], 5):
                most_accurate = key
        # Check if there was a match in this pair. If there was,
        # we can add the match to the protein and iterate one step more.
        # If not, we must flip the order of the second pair to match
        # b-ions withb-ions and y-ions with y-ions.
        # Flipping the order also requires
        # the index and protein to be reset.
        if not most_accurate:
            # Flip ion order, sort, then start from the beginning
            pairs[index + 1] = (pairs[index + 1][1], pairs[index + 1][0])
            pairs.sort()
            index = 0
            protein = ''
        else:
            protein += weight_to_acid[most_accurate]
            index += 1
    print(protein)
    return


if __name__ == "__main__":
    main()

