#
# @lc app=leetcode id=3349 lang=python3
#
# [3349] Adjacent Increasing Subarrays Detection I
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        dq = deque()
        available = set()
        for i in range(len(nums)):
            while dq and dq[0] <= i - k: dq.popleft()
            while dq and nums[dq[-1]] >=  nums[i]: dq.pop()
            dq.append(i)
            if len(dq) == k:
                if i - k in available: return True
                available.add(i)
        return False
# @lc code=end

