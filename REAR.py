# Copyright 2019 Jason Kim. All rights reserved.
# REAR.py
# My solution to REAR of the Rosalind Project.
# Jason Kim
# 7/31/2019
from collections import deque
import sys


# I credit neex on GitHub for my inspiration on this
# double-queue solution to find the match in the middle.
# https://github.com/neex/rosalind/blob/master/rear.py
# I devised a single-queue exact algorithm, but it took
# way too long to solve in 5 minutes due to the exponential
# growth when generating permutations.
def all_reversals(arr):
    reversals = []
    for start in range(len(arr) - 1):
        for end in range(start + 1, len(arr)):
            # Choose a substring to reverse
            rev_part = arr[start:end + 1]
            # Reverse, stitch, and add to list.
            reversals.append(arr[:start] + rev_part[::-1]
                   + arr[end + 1:])
    return reversals


# Returns the reversal distance between the two lists,
# first and second.
def reversal_dist(first, second):
    # Keep track of the minimum reversal distance.
    min_reversal_dist = sys.maxsize
    # Base case - distance is zero if they're equal.
    if first == second:
        return 0
    # First queue: start from first, try to match second.
    # Declare a hash table to keep track of the sequences
    # that have been seen from the queue, along with their
    # reversal distance as the values.
    seen_firstq = {
        first: 0
    }
    firstq = deque([first])
    # Loop while queue is not empty.
    while firstq:
        # Pop the front, and look it up in the hash table to
        # fetch its reversal distance.
        front = firstq.popleft()
        dist = seen_firstq[front]
        # Get all possible reversals of the front.
        for arr in all_reversals(front):
            # If this generated reversal is second, just return
            # the current reversal distance plus one.
            if arr == second:
                return dist + 1
            # And if this reversal was not seen, add the entry to
            # the hash table with the current reversal distance plus one.
            if arr not in seen_firstq:
                seen_firstq[arr] = dist + 1
                # Indeed, 4 seems to be the magic number of reversal
                # distances here, but there has been no explanation why this is so.
                # I believe I have one - this is because a sequence of length n
                # can have a maximum reversal distance of n - 1.
                # Since all sequences have length 10, max reversal distance
                # is 9. Thus each queue just needs to store reversal distances
                # and their respective sequences from each end up to 5.
                # Since the maximum dist of front is 3 for arr to be appended,
                # If seen_firstq[arr] = dist + 1 and this if statement below
                # is triggered then a sequence with reversal distance of 4 is
                # appended to the queue. Then the maximum reversal distance that
                # can be inside seen_firstq is 4 + 1 = 5.
                if dist < 4:
                    firstq.append(arr)
    # Second queue: start from second, try to match first.
    # Declare another hash table to keep track of the sequences
    # that have been seen from the second queue along with their
    # reversal distance as the values.
    seen_secondq = {
        second: 0
    }
    secondq = deque([second])
    # Loop while second queue is not empty.
    while secondq:
        # Pop the front, and look it up in the hash table to
        # fetch its reversal distance.
        front = secondq.popleft()
        dist = seen_secondq[front]
        # The first hash table stores reversal distances of up to 5.
        # When dist = x, reversal distance of x + 1 can be stored
        # in the second hash table. Since the maximum reversal distance
        # is 9, dist must only be calculated up to 3. Thus break the loop
        # when dist reaches 4.
        if dist >= 4:
            break
        # Apart from this, repeat what we did in the first queue.
        # Generate all reversals of front.
        for arr in all_reversals(front):
            # If the generated reversal is equal to first, we are done.
            if arr == first:
                return dist + 1
            # If the generated reversal was not seen before, add it
            # to the hash table w/ reversal distance of dist + 1.
            if arr not in seen_secondq:
                seen_secondq[arr] = dist + 1
                # For the same reason as before, append only if
                # dist is less than 4.
                if dist < 4:
                    secondq.append(arr)
            # ONE LAST THING: If this generated reversal IS IN
            # the first hash table, then we have a MATCH! The reversal
            # distance is the sum of the two reversal distances from each end.
            # Update the minimum as well.
            if arr in seen_firstq:
                min_reversal_dist = min(min_reversal_dist,
                                        seen_firstq[arr] + seen_secondq[arr])
    # Finally, return the minimum.
    return min_reversal_dist


def main():
    file = open("rosalind_rear.txt", "r")
    lines = file.readlines()
    file.close()
    # Strip carriage returns off each line.
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '')
    # Iterate through lines in reverse, popping empty lines
    # to avoid index hazard.
    for j in range(len(lines) - 1, -1, -1):
        if lines[j] == '':
            lines.pop(j)
    # Then convert each line to a tuple for hashing.
    # Hash table can't accept a list as a key.
    for k in range(len(lines)):
        lines[k] = tuple(lines[k].split(' '))
    # Start calculating reversal distance.
    # Loop over lines, but two at a time.
    for m in range(1, len(lines), 2):
        first = lines[m - 1]
        second = lines[m]
        dist = reversal_dist(first, second)
        print(dist, end=' ')
    return


if __name__ == "__main__":
    main()

