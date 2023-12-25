#
# @lc app=leetcode id=321 lang=python3
#
# [321] Create Maximum Number
#

# @lc code=start
from typing import List


class Solution:
    '''
    We do not know how many elements are in the final subsequence are from nums1 and nums2 respectively. So we just need to optimize
    However, we know if we are given k and nums1, we have the solution already from Leetcode 1673. Find the Most Competitive Subsequence, except in here we want the opposite
    '''
    
    '''
    Use monotonic increasing stack to tackle the problem.
    When the incoming number is smaller than stack[-1], we can pop from the stack if we can ensure we replace stack[-1] with nums[i:], we have enough elements to get to length of k
    '''
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        n = len(nums)
        for i, num in enumerate(nums):
            while stack and num > stack[-1] and n - i + len(stack) - 1 >= k:
                stack.pop()
            stack.append(num)
        return stack[:k]
    
    def mergeSubsequences(self, seq1, seq2):
        result = []
        i, j = 0, 0
        while i < len(seq1) and j < len(seq2):
            if seq1[i] > seq2[j]:
                result.append(seq1[i])
                i += 1
            elif seq1[i] < seq2[j]:
                result.append(seq2[j])
                j += 1
            else:
                i1, j1 = i + 1, j + 1
                while i1 < len(seq1) and j1 < len(seq2):
                     if seq1[i1] != seq2[j1]: break
                     else: 
                        i1 += 1
                        j1 += 1
                if i1 == len(seq1) or (j1 < len(seq2) and seq1[i1] < seq2[j1]):
                    result.append(seq2[j])
                    j += 1
                else:
                    result.append(seq1[i])
                    i += 1
        while i < len(seq1):
            result.append(seq1[i])
            i += 1
        while j < len(seq2):
            result.append(seq2[j])
            j += 1
        return result
    
    def findMax(self, result1, result2):
        n = len(result1)
        for i in range(n):
            if result1[i] > result2[i]:
                return result1
            elif result1[i] < result2[i]:
                return result2
        return result1


    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        useOnelowerLimit = max(0, k - len(nums2))
        useOneUpperLimit = min(len(nums1), k)
        result = [0] * k
        for i in range(useOnelowerLimit, useOneUpperLimit + 1, 1):
            nums1MaxSubSeq = self.mostCompetitive(nums1, i)
            nums2MaxSubSeq = self.mostCompetitive(nums2, k - i)
            current = self.mergeSubsequences(nums1MaxSubSeq, nums2MaxSubSeq)
            result = self.findMax(result, current)
        return result
# @lc code=end

