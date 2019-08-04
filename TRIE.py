# Copyright 2019 Jason Kim. All rights reserved.
# TRIE.py
# My solution to TRIE of the Rosalind Project.
# Jason Kim
# 8/4/2019


# I cite GeeksForGeeks' OOP structure for a trie as my guidance.
# https://www.geeksforgeeks.org/trie-insert-and-search/
class Node:
    # Constructor for node
    def __init__(self, num):
        # Children are references in an array of size 4.
        # Index 0 = A, 1 = T, 2 = G, 3 = C.
        self.children = [None] * 4
        # Id is assigned by Trie class.
        self.id = num


class Trie:
    # Constructor for trie
    def __init__(self):
        # Call Node's ctor to initialize its root node.
        # root ID is one. For every subsequent Node added,
        # increment the id counter.
        self.root = Node(1)
        self.id_counter = 2

    # Converts A, T, G, C to 0, 1, 2, 3.
    @staticmethod
    def ord_char(char):
        if char == 'A':
            return 0
        elif char == 'T':
            return 1
        elif char == 'G':
            return 2
        elif char == 'C':
            return 3
        else:
            raise Exception()

    # Converts 0, 1, 2, 3 to A, T, G, C.
    @staticmethod
    def char_ord(num):
        if num == 0:
            return 'A'
        elif num == 1:
            return 'T'
        elif num == 2:
            return 'G'
        elif num == 3:
            return 'C'
        else:
            raise Exception()

    # Inserts words inside the trie, making new nodes if necessary.
    def insert(self, word):
        node_ptr = self.root
        # Iterate over word, char by char
        for i in range(len(word)):
            order = self.ord_char(word[i])
            # Add a child node if word[i] is not represented
            if not node_ptr.children[order]:
                node_ptr.children[order] = Node(self.id_counter)
                self.id_counter += 1
            # Then change node_ptr to child
            node_ptr = node_ptr.children[order]


# Prints the adjacency list of a trie rooted at node_ptr.
def adj_list(node_ptr):
    # Base case: If node has no children, return.
    if node_ptr.children.count(None) == len(node_ptr.children):
        return
    for i in range(len(node_ptr.children)):
        # Find all children of this node.
        if node_ptr.children[i] is not None:
            child_ptr = node_ptr.children[i]
            # Convert children list index to base.
            base = Trie.char_ord(i)
            print(str(node_ptr.id) + ' ' + str(child_ptr.id)
                  + ' ' + base)
            # Call tree-recursively on each child.
            adj_list(child_ptr)


def main():
    file = open("rosalind_trie.txt", "r")
    data = file.readlines()
    file.close()
    for i in range(len(data)):
        data[i] = data[i].strip()
    trie = Trie()
    for seq in data:
        trie.insert(seq)
    adj_list(trie.root)
    return


if __name__ == "__main__":
    main()
