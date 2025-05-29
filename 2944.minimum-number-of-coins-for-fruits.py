#
# @lc app=leetcode id=2944 lang=python3
#
# [2944] Minimum Number of Coins for Fruits
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        heap = []
        n = len(prices)
        for i in range(n - 1, -1 , -1):
            while heap and heap[0][1] > 2 * i + 2: heapq.heappop(heap)
            current = prices[i]
            if heap and 2 * i + 2 < n: current += heap[0][0]
            heapq.heappush(heap, [current, i])
            if i == 0: return current
        return -1
# @lc code=end

