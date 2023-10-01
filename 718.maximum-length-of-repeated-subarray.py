#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#

# @lc code=start

from typing import List


class Solution:
    '''
    Binary searching for the answer and conducting subarray comparison by rolling hash
    Base chosen: must be larger than maximum of nums1 and nums2; preferably prime
    Mod: large enough to avoid overflow, should be prime
    Generate a lookup table for pow(self.base, 0:len(s)) % self.MOD              
    '''
  
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
    
    def getAllHashOfSize(self, nums, seen, size):
        h = 0
        for i in range(len(nums) - size + 1):
            h = self.rolling_hash(nums, i, size, h)
            if h not in seen:
                seen[h] = []
            seen[h].append(i)
        return seen
    
    def canFindSameHashSubArray(self, source, destination, seen, size):
        h = 0
        for i in range(len(destination) - size + 1):
            h = self.rolling_hash(destination, i, size, h)
            if h in seen:
                for j in seen[h]:
                    if source[j:j+size] == destination[i:i+size]:
                        return True
        return False

    def foundSubArray(self, size):
        seen = self.getAllHashOfSize(self.nums1, {}, size)
        return self.canFindSameHashSubArray(self.nums1, self.nums2, seen, size) 
    
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n, self.base, self.MOD = len(nums1), len(nums2), 101, pow(2,31) - 1
        self.nums1 = nums1
        self.nums2 = nums2

        self.base, self.MOD = 101, pow(2,31) - 1

        self.lookup = []
        seed = 1
        for i in range(min(m, n)):
            self.lookup.append(seed)
            seed *= self.base
            seed %= self.MOD
        
        left, right = 0, min(m, n) + 1
        while left < right:
            mid = left + (right - left) // 2
            if self.foundSubArray(mid):
                left = mid + 1
            else:
                right = mid
        return left - 1
# @lc code=end

