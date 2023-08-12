#
# @lc app=leetcode id=1847 lang=python3
#
# [1847] Closest Room
#

# @lc code=start
from typing import List

from sortedcontainers import SortedList


class Solution:
    '''
    We have two quantities we want to be sorted: roomId and size, such that binary search be carried out.
    As we know all queries before hand, we can first sort queries by minSize going from large to small and store the indices and preferred room.
    To ensure for each queries[i], we want the current tree to only contain rooms with size larger or equal to queries[i]. First sort rooms from large to small size and mark which next room to put into the tree
    In the tree, we keep the roomId in sorted order inside a sortedlist. Then we binary search for preferred's neighboring elements inside the tree, and choose the one with smaller difference.
    '''
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        queries = sorted([[query[1], query[0], i] for i, query in enumerate(queries)], key = lambda x: -x[0])

        NotYetInserted = 0
        rooms.sort(key = lambda x: -x[1])
        tree = SortedList()
        result = [-1] * len(queries)
        for minSize, preferred, ind in queries:
            while NotYetInserted < len(rooms) and rooms[NotYetInserted][1] >= minSize:
                tree.add(rooms[NotYetInserted][0])
                NotYetInserted += 1
            if len(tree) > 0:
                bisectLeftInd = tree.bisect_left(preferred)
                alternatives = []
                if bisectLeftInd < len(tree):
                    alternatives.append([abs(preferred - tree[bisectLeftInd]), tree[bisectLeftInd]])
                if bisectLeftInd > 0:
                    alternatives.append([abs(preferred - tree[bisectLeftInd - 1]), tree[bisectLeftInd - 1]])
                alternatives.sort()
                if alternatives:
                    result[ind] = alternatives[0][1]
        return result

# @lc code=end

