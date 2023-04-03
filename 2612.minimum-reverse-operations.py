#
# @lc app=leetcode id=2612 lang=python3
#
# [2612] Minimum Reverse Operations
#

# @lc code=start
from collections import deque
from typing import List
import sortedcontainers

class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        result = [-1]*n
        slOdd = SortedList()
        slEven = SortedList()
        bannedSet = set(banned)
        for i in range(n):
            if i not in bannedSet:
                if i % 2 == 1:
                    slOdd.add(i)
                else:
                    slEven.add(i)

        dq = deque()
        dq.append([p, 0])
        if p % 2 == 1:
            slOdd.remove(p)
        else:
            slEven.remove(p)
        while dq:
            i, flip = dq.popleft()
            result[i] = flip
            lowerLimit = 2*max(0, i - k + 1) + k - 1 - i
            upperLimit = 2*min(i + 1, n + 1 - k) + k - 3 - i
            tree = slOdd if (k - 1 - i) % 2 == 1 else slEven
            lstToRemove = list(tree.irange(lowerLimit, upperLimit))
            for j in lstToRemove:
                tree.remove(j)
                dq.append([j, flip + 1])         
        return result
# @lc code=end

