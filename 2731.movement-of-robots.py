#
# @lc app=leetcode id=2731 lang=python3
#
# [2731] Movement of Robots
#

# @lc code=start
from typing import List


class Solution:
    '''
    The rule is the same as robots passing through each other.
    '''
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        data = []
        for num, c in zip(nums, s):
            if c == 'L': data.append(num - d)
            else: data.append(num + d)
        data.sort()
        MOD = 1000000007
        n = len(data)
        result = 0 
        for i, num in enumerate(data):
            result += num * i
            result -= num * (n - i - 1)
            result %= MOD
        return result

# @lc code=end
