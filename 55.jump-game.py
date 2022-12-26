#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
from typing import List


class Solution:
    # Instead of trying to construct possible paths from left to right, what if we think backward?
    # Do we need to traverse every possible path to reach the end (that would be at least O(N^2))
    # No! We just need to find out if it is possible
    # like this array: [1,4,0,2,0,0], even if we will have more jump steps if we use 2, the bool result is unaffected. On the other hand, we can go for an iterative algorithm
    
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        position = n-1
        for i in range(n-2, -1,-1):
            if nums[i]+i >= position:
                position = i
            #print(i, position)
        return position == 0
# @lc code=end

