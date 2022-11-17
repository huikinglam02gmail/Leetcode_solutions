#
# @lc app=leetcode id=223 lang=python3
#
# [223] Rectangle Area
#

# @lc code=start
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        if ax1 > bx1:
            ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 = bx1, by1, bx2, by2, ax1, ay1, ax2, ay2
        area_a = ((ax2-ax1)*(ay2-ay1))
        area_b = ((bx2-bx1)*(by2-by1))
        if (by2 >= ay1 and ax2 >= bx1 and by1 <= ay1) or (ay2 >= by1 and ax2 >= bx1 and by2 >= ay2):
            return area_a + area_b - (min(ay2,by2) - max(ay1,by1))*(min(ax2,bx2) - max(ax1,bx1))      
        elif by1 >= ay1 and by2 <= ay2 and ax2 >= bx1:
            return area_a + area_b - (by2-by1)*(min(bx2,ax2)-bx1)
        else:
            return area_a + area_b
# @lc code=end

