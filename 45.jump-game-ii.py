#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
from typing import List


class Solution:
    # This problem is different from Jump Game because one can always reach the end
    # In first round, we can reach between left = 0 and right = nums[0]
    # We found out where is the furthest that I can get, which would set the maximum jump span in the next step
    # Afterwards in each round, left_new = right; right_new = max(i + nums[i]) for i between left and right
    def jump(self, nums: List[int]) -> int:
        left, right, jumps = 0, 0, 0
        while right < len(nums)-1:
            jumps += 1
            nextRight = left
            for i in range(left, right + 1):
                nextRight = max(nextRight, i + nums[i])
            left, right = right, nextRight
        return jumps
# @lc code=end

