#
# @lc app=leetcode id=1701 lang=python3
#
# [1701] Average Waiting Time
#

# @lc code=start
from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        accu = 0
        result = []
        for arrival, time in customers:
            if accu < arrival:
                accu = arrival
            accu += time
            result.append(accu - arrival)
        return sum(result) / len(result)
# @lc code=end

