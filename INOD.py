# Copyright 2019 Jason Kim. All rights reserved.
# INOD.py
# My solution to INOD of the Rosalind Project.
# Jason Kim
# 7/30/2019
import math


def main():
    file = open("rosalind_inod.txt", "r")
    n = int(file.readline().replace('\n', ''))
    file.close()
    # Wikipedia: In an unrooted binary tree with n leaves
    # there will be n-2 internal nodes.
    # Base cases: 2 leaves have 0 internal nodes because ther
    # cannot be a node with degree 2 (either 1 or 3).
    # 3 leaves have 1 internal node because there must be another
    # node connecting those leaves together with degree 3, since again
    # there cannot be a node of degree 2.
    # Inductive step: For an unrooted binary tree with n leaf nodes,
    # assume it is true that it has n-2 internal nodes.
    # Then, for this unrooted binary tree to have n + 1 leaf nodes,
    # two child nodes must be added to an existing leaf node, because there
    # cannot be a node of degree 2. One of the children becomes the nth leaf
    # node, and the other child becomes the (n + 1)th leaf node.
    # Consequently, the old existing leaf node to which two child nodes were added
    # now has degree 3, so it becomes an internal node.
    # The tree had n-2 internal nodes and now it has one more, leading to
    # n-1 internal nodes and n+1 leaf nodes. Since (n + 1) - 2 = n - 1,
    # the unrooted binary tree with n+1 leaf nodes also has two less
    # internal nodes than it has leaf nodes.
    print(n - 2)
    return


if __name__ == "__main__":
    main()

