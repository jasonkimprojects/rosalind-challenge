# Copyright 2019 Jason Kim. All rights reserved.
# NKEW.py
# My solution to NKEW of the Rosalind Project.
# Jason Kim
# 8/7/2019


# Workaround for the map function
def strip(string):
    return string.strip()


# Finds the left and right order of the vertices,
# along with their indices in the tree string.
def order(tree, node1, node2):
    idx1 = tree.find(node1)
    idx2 = tree.find(node2)
    if idx1 < idx2:
        # node1 is the left node
        return (node1, idx1), (node2, idx2)
    else:
        # node2 is the left node
        return (node2, idx2), (node1, idx1)


# Finds the first number in the tree after pos.
def first_number(tree, pos):
    delimiters = [',', ')', ';']
    search_str = tree[pos:]
    index = 0
    while search_str[index] not in delimiters:
        index += 1
    return float(search_str[:index])


# Finds the weighted Newick distance.
def find_distance(tree, vertices):
    # Guaranteed to have 2 elements.
    nodes = vertices.split(' ')
    # Base case: if the nodes are the same, distance is 0.
    if nodes[0] == nodes[1]:
        return 0
    # Then get the left and right ends.
    left, right = order(tree, nodes[0], nodes[1])
    # Get the weight of the left node.
    # First get the starting index, which is the
    # index of the node plus the len(name of
    # the left node) plus the : delimiter (1).
    weight_left = first_number(tree, left[1] + len(left[0]) + 1)
    # Start matching parentheses.
    stack = []
    # Stack will contain tuples of ( '(' or ')', index).
    search_str = tree[left[1]:right[1]]
    # Search just between the two nodes.
    for i in range(len(search_str)):
        if search_str[i] in ['(', ')']:
            if len(stack) == 0:
                # Don't index top of stack if empty
                stack.append((search_str[i], i))
            else:
                # If parentheses match, get rid of the pair.
                if stack[-1][0] == '(' and search_str[i] == ')':
                    stack.pop()
                else:
                    stack.append((search_str[i], i))
    # At this point, stack contains mismatched parentheses only.
    # Sum the weights of the mismatched parentheses.
    parent_weights = 0.0
    for pair in stack:
        # For right parentheses, it's the first number after it.
        if pair[0] == ')':
            # pair[1] is the index of ). So +1 is :, +2 is the first digit.
            parent_weights += first_number(search_str, pair[1] + 2)
        else:
            # For left parentheses, it's the first number after the
            # matching ). We need to find it, but it may NOT be in
            # search_str. So we need to look at the whole tree and convert
            # the index of the ( in the perspective of the whole tree.
            converted_index = pair[1] + left[1]
            temp_stack = [('(', converted_index)]
            for i in range(converted_index + 1, len(tree)):
                if tree[i] in ['(', ')']:
                    if temp_stack[-1][0] == '(' and tree[i] == ')':
                        temp_stack.pop()
                        # If that was the last pop, this is the index we
                        # are looking for!
                        if len(temp_stack) == 0:
                            parent_weights += first_number(tree, i + 2)
                            break
                    else:
                        temp_stack.append((tree[i], i))
    # Final step: if there is a comma after the last mismatched ),
    # add the weight of right.
    # Go through the stack again to find the last mismatched ).
    last_mismatched_right = 0
    for pair in stack:
        if pair[0] == ')' and pair[1] > last_mismatched_right:
            last_mismatched_right = pair[1]
    # Then look through search_str after last_mismatched_right for a comma.
    for j in range(last_mismatched_right + 1, len(search_str)):
        if search_str[j] == ',':
            weight_right = first_number(tree, right[1] + len(right[0]) + 1)
            print(int(weight_left + parent_weights + weight_right), end=' ')
            return
    print(int(weight_left + parent_weights))
    return


def main():
    file = open("rosalind_nkew.txt", "r")
    data = list(map(strip, file.readlines()))
    file.close()
    for i in range(0, len(data) - 1, 3):
        find_distance(data[i], data[i + 1])
    return


if __name__ == "__main__":
    main()

