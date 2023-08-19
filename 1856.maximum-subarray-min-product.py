#
# @lc app=leetcode id=1856 lang=python3
#
# [1856] Maximum Subarray Min-Product
#

# @lc code=start
from typing import List


class Solution:
    '''
    Think step by step.
    We should consider all subarrays starting with nums[0]. For 0 < i < n, as long as nums[i] >= nums[0], the min product will be prefixSum[i] * nums[0]. When we arrive at nums[i] < nums[0], the min product will become prefixSum[j] * nums[i] for j >= i. Therefore, we only care about the smaller number on the right, a monotonic nondecreasing stack would serve the purpose.
    For example, nums = [3,1,5,6,4,2]. We know all subarrays starting from 3 cannot have 3 as min factor past 1 on the right. So we save 3 * 3.
    After nums is processed, we clear the stack and record each popped element as the min factor and sum until the stack top as the max sum. To do that easily at -1 at the end of nums
    '''
    def maxSumMinProduct(self, nums: List[int]) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        stack = []
        stack.append(-1)
        nums.append(-1)
        result, MOD = 0, pow(10, 9) + 7
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                result = max(result, nums[stack.pop()] * (prefix[i] - prefix[stack[-1] + 1]))
            stack.append(i)
        return result % MOD
# @lc code=end

