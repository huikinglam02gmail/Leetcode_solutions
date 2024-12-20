#
# @lc app=leetcode id=3388 lang=python3
#
# [3388] Count Beautiful Splits in an Array
#

# @lc code=start
from typing import List


class Solution:
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
    
    def numberOfBeautifulSplits(self, nums, size):
        h = 0
        seen = {}
        result = 0
        for i in range(len(nums) - size + 1):
            h = self.rolling_hash(nums, i, size, h)
            if h not in seen: seen[h] = set()
            if i - size in seen[h]: 
                if i == size: #nums1 start at i - size (0) and nums2 starts at i
                    result += len(nums) - i - size
                    self.usedAsNums2.add(i)
                elif i - size not in self.usedAsNums2: #nums2 start at i - size and nums3 starts at i
                    result += 1
            seen[h].add(i)
        return result
    
    '''
    ceil division
    '''
    def ceildiv(self, a, b):
        return -(a // -b)

    def beautifulSplits(self, nums: List[int]) -> int:
        self.base, self.MOD = 53, pow(2,31) - 1

        self.lookup = []
        seed = 1
        for i in range(len(nums)):
            self.lookup.append(seed)
            seed *= self.base
            seed %= self.MOD

        self.usedAsNums2 = set()
        result = 0
        for size in range(1, self.ceildiv(len(nums), 2), 1): result += self.numberOfBeautifulSplits(nums, size)
        return result

# @lc code=end

