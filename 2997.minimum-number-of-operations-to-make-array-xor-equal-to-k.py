#
# @lc app=leetcode id=2997 lang=python3
#
# [2997] Minimum Number of Operations to Make Array XOR Equal to K
#

# @lc code=start
from typing import List


class Solution:
    '''
    break down k into binary representation
    for each num, add # of 0 and 1 bits in each slot.
    '''
    def minOperations(self, nums: List[int], k: int) -> int:
        bitsToUse = len(bin(k)[2:])
        for num in nums: bitsToUse = max(bitsToUse, len(bin(num)[2:]))
        counts = [0] * bitsToUse
        for num in nums:
            for i in range(bitsToUse):
                if num & (1 << i): counts[i] += 1
        result, n = 0, len(nums)
        for i in range(bitsToUse):
            if (not (k & (1 << i))) ^ (not counts[i] % 2): result += 1
        return result
    # @lc code=end

