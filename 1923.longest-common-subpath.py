#
# @lc app=leetcode id=1923 lang=python3
#
# [1923] Longest Common Subpath
#

# @lc code=start
from typing import List


class Solution:
    '''
    We can binary search for the answer. The range to search is [0, min(len(paths[i]))]
    '''
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        
# @lc code=end

