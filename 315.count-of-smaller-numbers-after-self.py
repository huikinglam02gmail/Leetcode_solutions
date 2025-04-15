#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#

# @lc code=start
from typing import List


class Solution:
    '''
    This is a typical merge sort question
    To answer the question, one simply needs to recall that in the merge step in merge sort, an element will encounter another element once, and the array got sorted in n log n time.
    mergesort(low, high) = mergesort(self.item[low:high])
    '''

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

