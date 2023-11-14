#
# @lc app=leetcode id=1981 lang=python3
#
# [1981] Minimize the Difference Between Target and Chosen Elements
#

# @lc code=start
from typing import List


class Solution:
    '''
    1 <= m, n <= 70
    1 <= mat[i][j] <= 70
    1 <= target <= 800
    So the largest Sum can only be 70 * 70 = 4900
    For each row, we can scan through 
    '''
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        current = set()
        current.add(0) 
        for row in mat:
            nxt = set()
            for i in row:
                for s in current:
                    nxt.add(i + s)
            current = nxt
        result = float("inf")
        for num in current:
            result = min(result, abs(target - num))
        return result
# @lc code=end

