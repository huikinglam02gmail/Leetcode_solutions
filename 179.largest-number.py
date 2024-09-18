#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
from functools import cmp_to_key
from typing import List


class Solution:
    '''
    If given three nonnegative integers a, b and c,
    if str(a) + str(b) > str(b) + str(a) and str(b) + str(c) > str(c) + str(b), we have str(a) + str(c) > str(c) + str(a)
    '''
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=cmp_to_key(lambda x, y: 1 if str(x)+str(y) < str(y)+str(x) else -1))
        result = "".join([str(num) for num in nums])
        i = 0
        while i < len(result) and result[i] == "0": i += 1
        return result[i:] if i < len(result) else "0"
        
# @lc code=end

