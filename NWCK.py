# Copyright 2019 Jason Kim. All rights reserved.
# NWCK.py
# My solution to NWCK of the Rosalind Project.
# Jason Kim
# 8/3/2019


# Helper function to determine if a node is enclosed within
# the given opening and closing parentheses (), passed
# as a tuple.
def is_between(node_pos, parentheses):
    return (node_pos > parentheses[0]) and (node_pos < parentheses[1])


# Helper function to populate node_list with tuples
# that hold the opening and closing parentheses ()
# which enclose node, in order from nearest from node
# to farthest from node.
def surrounding_parentheses(tree, node_pos, node_list):
    # Make two stacks, one for searching left from node_pos
    # and another for searching right from node_pos.
    # The stack will hold the indices of unbalanced (s
    # for the left search, and the indices of unbalanced )s
    # for the right search. During each search, if a matching
    # parenthese is encountered, the stack will be popped.
    # In Python, lists can be used as stacks, with the last
    # element functioning as the top. append() is push,
    # pop() is pop since it defaults to removing the last element
    # if an index is not passed.
    left_stack = []
    right_stack = []
    # Begin with left search (order doesn't matter, can start
    # with right search as well).
    for i in range(0, node_pos):
        if tree[i] == '(':
            left_stack.append(i)
        # ( comes before ), so no need to check if non-empty.
        elif tree[i] == ')':
            left_stack.pop()
    # Then go with right search, but in reverse since
    # ) comes before (.
    for j in range(len(tree) - 1, node_pos, -1):
        if tree[j] == ')':
            right_stack.append(j)
        elif tree[j] == '(':
            right_stack.pop()
    # Then left_stack and right_stack should have an identical
    # number of unbalanced parentheses. Sanity check.
    assert len(left_stack) == len(right_stack)
    # Now fill node_list with tuples by popping the top off
    # both stacks, while they are not empty.
    while left_stack:
        parentheses_tuple = (left_stack.pop(), right_stack.pop())
        node_list.append(parentheses_tuple)


# I am quite sure that I have invented a new algorithm
# to find distances in Newick format trees quickly,
# without converting them to nodes or distance matrices.
# I say this because I could not find my procedure elsewhere.
def find_dist(tree, node_one, node_two):
    # If the two nodes are equal, then their
    # distance is zero, trivially.
    if node_one == node_two:
        return 0
    # Then find the index of each node in the tree.
    node_one_pos = tree.find(node_one)
    node_two_pos = tree.find(node_two)
    # The two nodes MUST exist in the tree.
    assert node_one_pos != -1 and node_two_pos != -1
    # Create an empty list for each node. The lists will be
    # passed to surrounding_parentheses.
    node_one_list = []
    node_two_list = []
    # Pass them to the helper function.
    surrounding_parentheses(tree, node_one_pos, node_one_list)
    surrounding_parentheses(tree, node_two_pos, node_two_list)
    # If a node is root, the parentheses list is empty.
    # Check if either is the root. If node_one is root, then
    # the distance is the number of ()s (i.e. number of parents)
    # that node_two has. If node_two is root, then the distance
    # is the number of ()s that node_one has. Both cannot be
    # root because we already checked if the nodes are identical.
    if not node_one_list:
        return len(node_two_list)
    elif not node_two_list:
        return len(node_one_list)
    # Check if one node is the direct ancestor of the other node,
    # i.e. they can be connected by traversing the tree vertically
    # ONLY. No traversing across sibling nodes.
    # If they are directly related, then the distance is just the
    # number of edges from the successor to the predecessor.
    for x in range(len(node_one_list)):
        # The parent of the parentheses node is the index after the
        # closing ).
        parent_pos = node_one_list[x][1] + 1
        if parent_pos == node_two_pos:
            # Because x is zero-based, # of edges = x + 1.
            return x + 1
    for y in range(len(node_two_list)):
        parent_pos = node_two_list[y][1] + 1
        if parent_pos == node_one_pos:
            return y + 1
    # Otherwise, for each parentheses list, iterate from beginning
    # to end. Find the () at the earliest index that contains the
    # position of the other node in between. Then the traversal distance
    # to the common ancestor is (index + 1).
    node_one_dist = 0
    for a in range(len(node_one_list)):
        if is_between(node_two_pos, node_one_list[a]):
            node_one_dist = a + 1
            break
    node_two_dist = 0
    for b in range(len(node_two_list)):
        if is_between(node_one_pos, node_two_list[b]):
            node_two_dist = b + 1
            break
    # The total distance is their sum.
    return node_one_dist + node_two_dist


def main():
    file = open("rosalind_nwck.txt", "r")
    lines = file.readlines()
    file.close()
    for i in range(0, len(lines), 3):
        tree = lines[i]
        lines[i + 1] = lines[i + 1].strip().split(' ')
        node_one = lines[i + 1][0]
        node_two = lines[i + 1][1]
        print(find_dist(tree, node_one, node_two), end=' ')


if __name__ == "__main__":
    main()

