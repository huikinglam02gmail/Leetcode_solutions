#
# @lc app=leetcode id=995 lang=python3
#
# [995] Minimum Number of K Consecutive Bit Flips
#

# @lc code=start
from typing import List


class Solution:
    '''
    This is a seemingly hard question... looks like there're infinite ways of flipping!
    But if we tweak our thinking a little bit, flip = XOR -> flip twice = doing nothing
    So to solve the problem (without infinite flipping and never reaching the answer), we expect every leftmost 0 should be flipped at most once
    Then we can use this approach:
    Scan from left to right
    Whenever we see 0, we need to flip the next consecutive k elements
    This would lead to a O(nk) algorithm, which is slow.
    We can keep track of how many flips are there in the current sliding window by this approach:
    For example: nums = [0,0,0,1,0,1,1,0], k = 3
    i = 0: need switch, we modify the array, nums[i] += 2
    nums = [2,0,0,1,0,1,1,0], flips = 1
    i = 1: (flips & 1) ^ nums[i] = 1: no need do anything
    i = 2: (flips & 1) ^ nums[i] = 1: no need do anything
    i = 3: now we out of bound from i = 0.
    Check if nums[i] > 1. If so, decrease nums[i] by 2, and decrease flip by 1
    Then we just keep going. We return -1 if len(nums) - i < k    
    '''
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flips, n, result = 0, len(nums), 0
        for i in range(n):
            if i >= k and nums[i - k] > 1: flips -= 1
            if (flips & 1) ^ nums[i] == 0:
                if i > n - k: return -1
                flips += 1
                nums[i] += 2
                result += 1
        return result
# @lc code=end

