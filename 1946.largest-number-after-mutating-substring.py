#
# @lc app=leetcode id=1946 lang=python3
#
# [1946] Largest Number After Mutating Substring
#

# @lc code=start
from typing import List


class Solution:
    '''
    Classic greedy problem
    Find the leftmost index in which change[int(i)] >= int(i) and expand as much as possible
    '''
    def maximumNumber(self, num: str, change: List[int]) -> str:
        newNum = [int(c) for c in num]
        n = len(newNum)
        for i in range(n):
            j = i
            if newNum[j] < change[newNum[j]]:
                while j < len(newNum) and newNum[j] <= change[newNum[j]]:
                    newNum[j] = change[newNum[j]]
                    j += 1
            if j > i:
                return "".join([str(c) for c in newNum])
        return num
# @lc code=end

