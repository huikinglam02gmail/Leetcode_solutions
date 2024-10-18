#
# @lc app=leetcode id=2260 lang=python3
#
# [2260] Minimum Consecutive Cards to Pick Up
#

# @lc code=start
from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        result = float("inf")
        lastSeen = {}
        for i, card in enumerate(cards):
            if card in lastSeen: result = min(result, i - lastSeen[card] + 1)
            lastSeen[card] = i
        return -1 if result == float("inf") else result
        
# @lc code=end

