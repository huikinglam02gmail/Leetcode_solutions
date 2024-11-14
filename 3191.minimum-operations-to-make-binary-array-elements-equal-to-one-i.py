#
# @lc app=leetcode id=3191 lang=python3
#
# [3191] Minimum Operations to Make Binary Array Elements Equal to One I
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dq = deque()
        result = 0
        for num in nums:
            if len(dq) > 2: dq.popleft()
            toInsert = num
            if len(dq) == 2 and dq[0] == 0:
                dq[0] = 1 - dq[0]
                dq[1] = 1 - dq[1]
                toInsert = 1 - num
                result += 1
            dq.append(toInsert)
        while dq:
            if dq.popleft() != 1: return -1
        return result
        
# @lc code=end

