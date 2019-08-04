# Copyright 2019 Jason Kim. All rights reserved.
# SORT.py
# My solution to SORT of the Rosalind Project.
# Jason Kim
# 8/4/2019
from collections import deque
import sys
import copy


# all_reversals has been modified to return a hash table
# instead of a list. The keys are each reversal of arr,
# and the value is a tuple of (start, end) indicating
# which subsequence of arr was reversed.
def all_reversals(arr):
    reversals = {}
    for start in range(len(arr) - 1):
        for end in range(start + 1, len(arr)):
            # Choose a substring to reverse
            rev_part = arr[start: end + 1]
            # Reverse, and stitch.
            rev_tuple = arr[:start] + rev_part[::-1] + arr[end + 1:]
            # Add to hash table, recording start and end.
            reversals[rev_tuple] = (start, end)
    return reversals


# Returns the reversal distance between the two tuples
# first and second, and also the sequence of reversals
# that transforms first into second.
# Modified from my code for REAR.
def reversal_seq(first, second):
    # Keep track of the minimum reversal distance.
    min_reversal_dist = sys.maxsize
    # And also the reversal sequence.
    min_reversal_seq = []
    # Base case - distance is zero if they're equal,
    # and the sequence is an empty list.
    if first == second:
        return 0, []
    # First queue: start from first and try to match second.
    # Hash table keeps track of the sequences that were seen
    # from the queue as keys. The value is a tuple. First elt
    # in tuple is the reversal distance. Second elt in tuple is
    # a list of tuples. Each tuple in this list is a reversal,
    # represented by (start, end). Tuples are appended to list in
    # the order that the reversals are made.
    seen_firstq = {
        first: (0, [])
    }
    firstq = deque([first])
    # Loop while queue is not empty.
    while firstq:
        # Pop the front, lookup reversal distance
        front = firstq.popleft()
        dist = seen_firstq[front][0]
        # Get all possible reversals of the front i.e. traverse
        # the hash table by key.
        front_reversals = all_reversals(front)
        for key in front_reversals:
            # If this generated reversal is second, distance is
            # current reversal distance plus one. The reversal list
            # is the current list plus the value of this key.
            if key == second:
                final_dist = dist + 1
                final_seq = copy.deepcopy(seen_firstq[front][1])
                final_seq.append(front_reversals[key])
                return final_dist, final_seq
            # And if this reversal was not seen, add the entry to the hash table.
            # The reversal distance is dist + 1, while the reversal list is the
            # current list plus the value of this key.
            if key not in seen_firstq:
                final_dist = dist + 1
                final_seq = copy.deepcopy(seen_firstq[front][1])
                final_seq.append(front_reversals[key])
                seen_firstq[key] = (final_dist, final_seq)
                # See REAR.py for an explanation on selecting 4.
                if dist < 4:
                    firstq.append(key)
    # Second queue: start from second, try to match first.
    # seen_secondq keeps track of the sequences that were seen
    # from the second queue as keys. The values of the keys are the
    # same format as seen_firstq.
    seen_secondq = {
        second: (0, [])
    }
    secondq = deque([second])
    # Loop while second queue is not empty.
    while secondq:
        # Pop the front, lookup reversal distance
        front = secondq.popleft()
        dist = seen_secondq[front][0]
        # See REAR.py for an explanation on why loop breaks.
        if dist >= 4:
            break
        # Get all possible reversals of the front i.e. traverse
        # the hash table by key.
        front_reversals = all_reversals(front)
        for key in front_reversals:
            # If the generated reversal is first, we are done.
            if key == first:
                final_dist = dist + 1
                final_seq = copy.deepcopy(seen_secondq[front][1])
                final_seq.append(front_reversals[key])
                return final_dist, final_seq
            # And if this reversal was not seen, add the entry to seen_secondq.
            if key not in seen_secondq:
                final_dist = dist + 1
                final_seq = copy.deepcopy(seen_secondq[front][1])
                final_seq.append(front_reversals[key])
                seen_secondq[key] = (final_dist, final_seq)
                # See REAR.py for an explanation on selecting 4.
                if dist < 4:
                    secondq.append(key)
            # ONE LAST THING: If this generated reversal IS IN
            # the first hash table, then we have a MATCH! The reversal
            # distance is the sum of the two reversal distances from each end.
            # The reversal sequence is the list of seen_firstq[key] plus
            # the REVERSED list of seen_secondq[key].
            if key in seen_firstq:
                final_dist = seen_firstq[key][0] + seen_secondq[key][0]
                if final_dist < min_reversal_dist:
                    min_reversal_dist = final_dist
                    # Now form the final sequence.
                    final_seq = []
                    for item in seen_firstq[key][1]:
                        final_seq.append(item)
                    for item in reversed(seen_secondq[key][1]):
                        final_seq.append(item)
                    min_reversal_seq = final_seq
    # Finally, return the minimum and its sequence.
    return min_reversal_dist, min_reversal_seq


def main():
    file = open("rosalind_sort.txt", "r")
    first = tuple(map(int, file.readline().strip().split(' ')))
    second = tuple(map(int, file.readline().strip().split(' ')))
    file.close()
    distance, sequence = reversal_seq(first, second)
    print(distance)
    for item in sequence:
        # Why can't Rosalind use zero-based indexing, like we all do?
        print(str(item[0] + 1) + ' ' + str(item[1] + 1))
    return


if __name__ == "__main__":
    main()

