#
# @lc app=leetcode id=3186 lang=python3
#
# [3186] Maximum Total Damage With Spell Casting
#

# @lc code=start
from collections import deque
from collections import deque
import heapq
from typing import List


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        counts = {}
        for p in power:
            counts[p] = counts.get(p, 0) + 1
        powerSorted = sorted(counts.keys())
        heap = []
        temp = deque()
        for p in powerSorted:
            while temp and temp[0][0] <= p - 3:
                prevP, prevDamage = temp.popleft()
                heapq.heappush(heap, [- prevDamage, prevP])
            if heap:
                maxDamage = -heap[0][0]
                temp.append([p, maxDamage + p * counts[p]])
            else:
                temp.append([p, p * counts[p]])
        while temp:
            prevP, prevDamage = temp.popleft()
            heapq.heappush(heap, [- prevDamage, prevP])
        return - heap[0][0]
# @lc code=end

