#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
from typing import List


class Solution:
    '''
    First sort the nums
    Then use two pointer algorithm to find the closest 3 sum
    We can optimize the code by first checking the smallest and largest within the testing window [i+1:n]: nums[i] + (nums[i+1] + nums[i+2]) and nums[i] + (nums[n-2] + nums[n-1]) actually envelope target
    Otherwise we just proceed to the next i    
    '''

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result, n = float('inf'), len(nums)
        for i in range(n-2):
            S1 = nums[i] + nums[i+1] + nums[i+2]
            S2 = nums[i] + nums[n-2] + nums[n-1]
            candidates = [result, S1, S2]
            result = min(candidates, key = lambda x: abs(x-target))            
            if S1 <= target <= S2:
                left, right = i+1, n-1
                while left < right:
                    S = nums[i] + nums[left] + nums[right]
                    candidates = [result, S]
                    result = min(candidates, key = lambda x: abs(x-target))
                    if S == target:
                        return target
                    elif S < target:
                        left += 1
                    else:
                        right -= 1
        return result
# @lc code=end

