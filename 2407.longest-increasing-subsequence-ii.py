#
# @lc app=leetcode id=2407 lang=python3
#
# [2407] Longest Increasing Subsequence II
#

# @lc code=start
from typing import List

class MaxSegmentTree:
    def __init__(self, n, value) -> None:
        self.tree = [value]*n

    def update(self, i, val):
        i += len(self.tree) // 2
        self.tree[i] = val
        i //= 2
        while i > 0:
            self.tree[i] = max(self.tree[2*i], self.tree[2*i + 1])
            i //= 2
    
    def query(self, i, j):
        i += len(self.tree) // 2
        j += len(self.tree) // 2
        s = 0
        while i <= j:
            if i % 2 == 1:
                s = max(s, self.tree[i])
                i += 1
            if j % 2 == 0:
                s = max(s, self.tree[j])
                j -= 1
            i //= 2
            j //= 2
        return s      

class Solution:
    # In the contest initially I used a hash table to record maximum length of LIS ending with all possible num
    # At some point we need to know the maximum previous dp value for num - k <= i < num
    # While we can use sortedlist to search for keys in O(log N) time, the search for maximum dp value takes O(k) time
    # To save time on that, we can instead maintain a segment tree instead of dp table instead
    # The array segments are the range of possible keys   
    
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        result = 0
        dp = MaxSegmentTree(2*(max(nums) + 1), 0)
        
        for num in nums:
            i, j = max(0, num - k), num-1
            max_dp = dp.query(i,j) + 1
            result = max(result, max_dp)
            dp.update(num, max_dp)
        return result
# @lc code=end

