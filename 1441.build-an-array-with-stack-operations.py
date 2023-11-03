#
# @lc app=leetcode id=1441 lang=python3
#
# [1441] Build an Array With Stack Operations
#

# @lc code=start
from typing import List


class Solution:
    '''
    Just simulate    
    '''

    def buildArray(self, target: List[int], n: int) -> List[str]:
        result, j = [], 0
        for i in range(1, n + 1):
            result.append("Push")
            if i == target[j]:
                j += 1
            else:
                result.append("Pop")
            if j == len(target):
                return result
# @lc code=end

