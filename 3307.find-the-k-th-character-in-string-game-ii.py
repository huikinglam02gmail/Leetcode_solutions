#
# @lc app=leetcode id=3307 lang=python3
#
# [3307] Find the K-th Character in String Game II
#

# @lc code=start
from typing import List


class Solution:
    '''
    If len(operations) = n, the final string has the length 1 << n.
    Keep track of if k is operated on operation i or not.
    '''
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        result = 0
        k -= 1
        while k > 0:
            t = k.bit_length() - 1
            if operations[t]: result += 1
            k -= (1 << t)
        return chr(ord('a') + result % 26)

# @lc code=end

