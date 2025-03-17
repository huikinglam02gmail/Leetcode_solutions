#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
from typing import List


class Solution:
    '''
    Use hash table to store the numbers appearing in nums
    Then for each key, ask if the key is starting point of consecutive sequence and record length of sequence    
    '''

    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        result = 0
        for key in seen:
            if key - 1 not in seen:
                counter = 0
                current = key
                while current in seen:
                    counter += 1
                    current += 1
                result = max(result, counter)
        return result
# @lc code=end

