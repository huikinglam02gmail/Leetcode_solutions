#
# @lc app=leetcode id=2448 lang=python3
#
# [2448] Minimum Cost to Make Array Equal
#

# @lc code=start
from typing import List


class Solution:
    '''
    First, sort [num, cost] pairs according to num
    Then we can safely assume the final target is one of the nums
    The total cost is sum(abs(num-target)*cost) which we wish to minimize
    The absolute difference means if we are considering nums[i] at pivot, left of it is (nums[i] - nums[j])*cost[j] = (nums[i] * cost[i] - nums[j]* cost[j]) - nums[i]*(cost[i] - cost[j]) and right of it is (nums[j] - nums[i])*cost[j]
    Therefore it is advisable to keep the prefix sums of cost and num*cost
    This would allow for O(1) readout of change in costs    
    '''    
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)
        data = [[nums[i], cost[i]] for i in range(n)]
        data.sort()
        prefix_cost = [0]
        prefix_mult = [0]
        for num, c in data:
            prefix_cost.append(c + prefix_cost[-1])
            prefix_mult.append(num * c + prefix_mult[-1])
        result = float('Inf')
        for i in range(n):
            result = min(result, prefix_mult[-1] - prefix_mult[i+1] - prefix_mult[i] + data[i][0]*(prefix_cost[i] + prefix_cost[i+1] - prefix_cost[-1]))
        return result
# @lc code=end

