# Copyright 2019 Jason Kim. All rights reserved.
# CTBL.py
# My solution to CTBL of the Rosalind Project.
# Jason Kim
# 8/5/2019
from Bio import Phylo


def character_table(node, ordered_taxa):
    # Again, .clades? children? Direct access or accessor method?
    for child in node.clades:
        # Can't be a leaf node because it becomes a trivial character
        if not child.is_terminal():
            # Find all children of the internal node.
            arr = [0 for i in range(len(ordered_taxa))]
            for child_node in child.find_clades():
                if child_node.name:
                    # Raise flag to 1 in lexicographical order.
                    arr[ordered_taxa.index(child_node.name)] = 1
            # Print the array.
            for elt in arr:
                print(elt, end='')
            print()
            # Call recursively on each child.
            character_table(child, ordered_taxa)


# Using Biopython library to handle the parsing of newick trees
# Biopython documentation is HORRIBLE.
def main():
    tree = Phylo.read('rosalind_ctbl.txt', 'newick')
    nodes = []
    # Where does it say that no params defaults to all clades i.e.
    # "nodes", if you use standard tree terminology instead of
    # phylogenetic terms?
    for node in tree.find_clades():
        # And the documentation doesn't specify if name should be
        # accessed by an accessor (as in OOP encapsulation) or
        # by instance variable name directly - in this case it
        # is the latter, but where is your clarification?
        if node.name:
            nodes.append(node.name)
    nodes.sort()
    character_table(tree.root, nodes)
    return


if __name__ == "__main__":
    main()

