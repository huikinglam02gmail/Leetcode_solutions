#
# @lc app=leetcode id=1703 lang=python3
#
# [1703] Minimum Adjacent Swaps for K Consecutive Ones
#

# @lc code=start
from typing import List


class Solution:
    '''
    Remember one key point: the median of a sequence is where we should swap all sequence elements to if we want to make all elements equal and the number of +- 1 swaps is minimized (Leetcode 462).
    So we record occurence of 1 in nums. Then we consider length k subarrays of the indices array (loc) and decide how many swaps to create a consecutive k 1s around the median. Leetcode 462 tells us how many swaps to turn all of them to the median. To get k consecutives 1s around mid:
    1. if k is odd, number of moves = 2 * (1 + 2 + ... + (k - 1) // 2) = k // 2 * (k // 2 + 1)
    2. if k is even, number of moves = (1 + 2 + ... + k // 2) + (1 + 2 + ... + (k - 2) // 2) = (k // 2) * (k // 2)
    Since k can be large, using the 462 algorithm can be time consuming O(nk). If we look carefully at the formula, minMoves2(nums) = nums[-1] - nums[0] + nums[-2] - nums[1] +... :
    1. if n is odd: minMoves(nums) = (nums[mid + 1] +... + nums[-1]) - (nums[mid - 1] + nums[mid - 2] + ... + nums[0])
    2. if n is even: minMoves(nums) = (nums[mid] +... + nums[-1]) - (nums[mid - 1] + nums[mid - 2] + ... + nums[0])
    We can prepare prefix sum array to quickly calculate the output of Leetcode 462
    '''
    def minMoves(self, nums: List[int], k: int) -> int:
        prefix = [0]
        for i in range(len(nums)):
            if nums[i] == 1:
                prefix.append(prefix[-1] + i)
        result = float("Inf")
        for i in range(len(prefix) - k):
            result = min(result, prefix[i + k] + prefix[i] - prefix[i + (k+ 1) // 2] - prefix[i + k // 2]- (k // 2) * ((k + 1) // 2))
        return result
        
# @lc code=end

