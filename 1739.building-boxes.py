#
# @lc app=leetcode id=1739 lang=python3
#
# [1739] Building Boxes
#

# @lc code=start
class Solution:
    '''
    If box x is placed on top of the box y, then each side of the four vertical sides of the box y must either be adjacent to another box or to a wall.
    To minimize number of boxes on floor, we have to stack the boxes up. But we can only stack up like a quarter-pyramid side by side with the walls. To maximize number of boxes on top, we have to make the floor base with the same dimension.
    1st level = 1
    2nd level = 1 + 2
    3rd level = 1 + 2 + 3
    So we are looking for  n = 1 + (1 + 2) + ... + (1 + 2 + ... + i) + extra
    For the remaining extra, we first append to the bottom corner, and then add from bottom to top, sweeping across the pyramid. The number of boxes on the floor is the first minimum j in which 1 + (1 + 2) +.. + (1 + 2 + ... + j) > extra
    Return (1 + 2 + ... + i) + j
    '''
    def minimumBoxes(self, n: int) -> int:
        cur = 0
        nxt = 1
        lastSize = 1
        while n > cur + nxt:
            cur += nxt
            lastSize += 1
            nxt += lastSize
        
        remainder = 0
        while cur + remainder < n:
            cur += remainder
            remainder += 1
        return nxt + remainder - lastSize

# @lc code=end

