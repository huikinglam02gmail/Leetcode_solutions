#
# @lc app=leetcode id=2179 lang=python3
#
# [2179] Count Good Triplets in an Array
#

# @lc code=start
from typing import List


class Solution:
    '''
    315 with a twist. Map nums1[i] == nums2[j]: i: j map.
    Then ask in the 
    '''
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        nums1Index = [-1] * n
        for i in range(n): nums1Index[nums1[i]] = i
        indexMap = [-1] * n
        for i in range(n): indexMap[nums1Index[nums2[i]]] = i
        leftSmallerCounts = self.countSmaller(indexMap)
        result = 0
        for i in range(1, n - 1): result += (indexMap[i] - leftSmallerCounts[i]) * (n - i - 1 - leftSmallerCounts[i])
        return result

    def mergesort(self, low, high):
        if low < high - 1:
            mid = (low + high) // 2
            self.mergesort(low, mid)
            self.mergesort(mid, high)
            self.merge(low, mid, high)
    
    def merge(self, low, mid, high):
        left = []
        right = []
        for i in range(low, mid): left.append(self.nums[i])
        for i in range(mid, high): right.append(self.nums[i])
        l, r, shift = 0, 0, 0
        while l < mid - low and r < high - mid:
            if left[l][1] <= right[r][1]:
                self.count[left[l][0]] += shift
                self.nums[low + l + r] = left[l]
                l += 1
            else:
                shift += 1
                self.nums[low + l + r] = right[r]
                r += 1
        while l < mid - low:
            self.count[left[l][0]] += shift
            self.nums[low + l + r] = left[l]
            l += 1
        while r < high - mid:
            self.nums[low + l + r] = right[r]
            r += 1            
        
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.count = [0] * n
        self.nums = [[i, nums[i]] for i in range(n)]
        self.mergesort(0, len(nums))
        return self.count
# @lc code=end

