#
# @lc app=leetcode id=2261 lang=python3
#
# [2261] K Divisible Elements Subarrays
#

# @lc code=start
from typing import List


class Solution:
    '''
    Use rolling hash of lengths 1 to n which satisfy at most k p-divisible numbers
    '''
    def __init__(self):
        self.base, self.MOD = 211, pow(2,31) - 1
        self.lookup = []

    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        prefix = [0]
        for num in nums:
            if num % p == 0: prefix.append(prefix[-1] + 1)
            else: prefix.append(prefix[-1])
        
        seed = 1
        for i in range(len(nums)):
            self.lookup.append(seed)
            seed *= self.base
            seed %= self.MOD
        
        result = 0
        for size in range(1, len(nums) + 1, 1):
            h = 0
            seen = set()
            for i in range(len(nums) - size + 1):
                h = self.rolling_hash(nums, i, size, h)
                if prefix[i + size] - prefix[i] <= k: seen.add(h)
            result += len(seen)
        return result

    def rolling_hash(self, arr, i, size, seed):
        h = seed
        if i == 0:
            for j in range(size):
                h *= self.base
                h += arr[i + j]
                h %= self.MOD
        else:
            h -= arr[i - 1] * self.lookup[size - 1]
            h *= self.base
            h += arr[i + size - 1]
            h %= self.MOD
        return h
        
# @lc code=end

