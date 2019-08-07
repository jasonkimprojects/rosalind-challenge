# Copyright 2019 Jason Kim. All rights reserved.
# LREP.py
# My solution to LREP of the Rosalind Project.
# Jason Kim
# 8/7/2019


class Node:
    def __init__(self, label, parent, substr):
        self.label = label
        self.parent = parent
        self.substr = substr
        self.children = []


class SuffixTree:
    def __init__(self):
        # Hash table to map node label to node pointer.
        self.nodes = {}
        self.root = None

    def add_node(self, label, parent, substr):
        if self.root is None:
            # Then make the parent (root node).
            root_node = Node(parent, None, '')
            self.nodes[parent] = root_node
            self.root = root_node
        # Add a child node to the parent.
        new_node = Node(label, self.nodes[parent], substr)
        self.nodes[label] = new_node
        self.nodes[parent].children.append(new_node)


# Recursively computes the number of children on a given node
# that are leaf nodes
def num_leafnodes(node):
    # Base case: node is a leaf
    if len(node.children) == 0:
        return 1
    else:
        total = 0
        for child_node in node.children:
            total += num_leafnodes(child_node)
        return total


# Recursively computes the path from this node to root, and returns
# the substring made from root to this node.
def get_substring(node, string):
    if node.parent is None:
        return string
    else:
        return get_substring(node.parent, node.substr + string)


# Working around the map function
def strip(string):
    return string.strip()


def main():
    file = open("rosalind_lrep.txt", "r")
    data = list(map(strip, file.readlines()))
    file.close()
    # Pop the sequence off data
    seq = data.pop(0)
    # Then pop k off data
    k = int(data.pop(0))
    # Then add the node data to the tree
    tree = SuffixTree()
    for line in data:
        params = line.split(' ')
        # Parent, this, start idx, length
        # start idx is 1-based, so subtract 1
        start_idx = int(params[2]) - 1
        length = int(params[3])
        substr = seq[start_idx:start_idx + length]
        tree.add_node(params[1], params[0], substr)
    # Then loop over nodes. Pick out the internal nodes.
    internal_nodes = []
    for label in tree.nodes:
        if len(tree.nodes[label].children) > 0:
            internal_nodes.append(label)
    # Then loop over internal nodes only.
    repeats = []
    for label in internal_nodes:
        # The number of occurrences of a particular suffix
        # is the number of leaf nodes that it has!
        if num_leafnodes(tree.nodes[label]) >= k:
            repeats.append(get_substring(tree.nodes[label], ''))
    # Then find the longest repeat.
    longest = ''
    for repeat in repeats:
        if len(repeat) > len(longest):
            longest = repeat
    print(longest)
    return


if __name__ == "__main__":
    main()

