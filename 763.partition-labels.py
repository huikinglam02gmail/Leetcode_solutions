#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
from typing import List


class Solution:
    '''
    Run through the array first, save the last appearance index of each character
    Then from start of string, use a two pointer technique: left and right indicate current scope of the window
    example: s = "ababcbacadefegdehijhklij"
    last['a'] = 8, left = 0 right = 8
    last['b'] = 5 < right, no action needed
    last['c'] = 7 < right, no action needed
    When reached i = right: append right - left + 1; left = right = right+1    
    '''

    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, c in enumerate(s): last[c] = i
        result = []
        left, right = 0, 0
        for i, c in enumerate(s):
            if last[c] > right: right = last[c]
            if i == right:
                result.append(right - left + 1)
                left, right = right + 1, right + 1
        return result
# @lc code=end

