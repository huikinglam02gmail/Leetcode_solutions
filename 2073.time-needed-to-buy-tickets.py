#
# @lc app=leetcode id=2073 lang=python3
#
# [2073] Time Needed to Buy Tickets
#

# @lc code=start
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        result = 0
        while tickets[k] > 0:
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    result += 1
                    tickets[i] -= 1
                if i == k and tickets[i] == 0:
                    return result
        return -1
# @lc code=end

