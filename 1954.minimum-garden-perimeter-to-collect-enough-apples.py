#
# @lc app=leetcode id=1954 lang=python3
#
# [1954] Minimum Garden Perimeter to Collect Enough Apples
#

# @lc code=start
import bisect


class Solution:
    '''
    Perimeter for each square is give by 8 * i, i = 0, 1, 2, ...
    Number of new apples added = 4 * {[i + ... + (i + i - 1)] + [(i + 1) + ... + (i + i)]} = 12 * i * i
    '''
    def minimumPerimeter(self, neededApples: int) -> int:
        i = 0
        while neededApples > 0:
            neededApples -= 12 * i * i
            i += 1
        return 8 * (i - 1)
        
# @lc code=end

