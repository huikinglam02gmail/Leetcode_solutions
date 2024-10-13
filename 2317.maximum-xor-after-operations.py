#
# @lc app=leetcode id=2317 lang=python3
#
# [2317] Maximum XOR After Operations 
#

# @lc code=start
from typing import List


class Solution:
    '''
    For each number, we can XOR it with its complement, to get all bits set to 1. Then num AND with that will get all 1s up to the max set bit. E.g. if num = 6 = "110", we can XOR it with 1 and after AND it becomes 7 = "111"
    In nums, the max XOR after all treated num would be: for each bit, count how many nums has is set. If the number of set bit is positive we can add 1 << i to the result 
    '''
    def maximumXOR(self, nums: List[int]) -> int:
        counts =  [0] * 27
        for num in nums:
            for i in range(27):
                if num & (1 << i) > 0: counts[i] += 1
        result = 0
        for i in range(27):
            if counts[i] > 0: result += 1 << i
        return result
# @lc code=end

