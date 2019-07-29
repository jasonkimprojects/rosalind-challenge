# Copyright 2019 Jason Kim. All rights reserved.
# TREE.py
# My solution to TREE of the Rosalind Project.
# Jason Kim
# 7/29/2019


def main():
    file = open("rosalind_tree.txt", "r")
    num_nodes = int(file.readline().replace('\n', ''))
    num_lines = sum(1 for line in file)
    # Array to keep track of the parent of each node.
    # If a node does not have a parent, its entry is -1.
    parent = [-1 for i in range(num_nodes)]
    # Rewind file pointer to the beginning
    # Discard first line
    file.seek(0)
    file.readline()
    # Read through the rest of the lines (excluding the first,
    # since it was already read in as num_nodes)
    for i in range(num_lines):
        adj_list = file.readline().split(' ')
        # Rosalind uses 1-based indexing. Convert to 0-based.
        start_node = int(adj_list[0]) - 1
        end_node = int(adj_list[1]) - 1
        # If the end node already has a parent:
        if parent[end_node] != -1:
            # Reverse the parents of the end node.
            # The start node will be the parent of the end node.
            new_parent = start_node
            # Go down the parent lineage until no parent is found.
            while parent[end_node] != -1:
                # The old parent will be the next node visited.
                old_parent = parent[end_node]
                # Assign to new parent.
                parent[end_node] = new_parent
                # Reassign new parent as the current node for the next iteration.
                new_parent = end_node
                # Then move to the old parent
                end_node = old_parent
            # Now the oldest ancestor has a parent
            parent[end_node] = new_parent
        else:
            parent[end_node] = start_node
    file.close()
    # Count the number of nodes which have no parent.
    # Then the minimum number of edges needed is that number minus one,
    # because you need to designate a root node (only node in tree with
    # no parent) and connect all the other subtrees to the root.
    num_nodes_noparent = 0
    for num in parent:
        if num == -1:
            num_nodes_noparent += 1
    min_edges = num_nodes_noparent - 1
    print(min_edges)
    return


if __name__ == "__main__":
    main()

