#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
from typing import List


class Solution:
    '''
    hash table to store the index of nums2 with the value as key
    Maintain a monotonic decreasing stack
    Whenever replace previous element, enter the next greater element to be the current one     
    '''
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_table, stack = {}, []
        next_greater = [-1 for i in range(len(nums2))]
        for i, num in enumerate(nums2):
            hash_table[num] = i
            while stack and num > stack[-1][1]: next_greater[stack.pop()[0]] = num
            stack.append([i, num])
            
        result = []
        for num in nums1: result.append(next_greater[hash_table[num]])
        return result
                            
# @lc code=end

