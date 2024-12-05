#
# @lc app=leetcode id=2337 lang=python3
#
# [2337] Move Pieces to Obtain a String
#

# @lc code=start
class Solution:
    def canChange(self, start: str, end: str) -> bool:
        p1, p2 = 0, 0
        while p1 < len(start) and start[p1] == "_": p1 += 1
        while p2 < len(end) and end[p2] == "_": p2 += 1
        while p1 < len(start) and p2 < len(end):
            if start[p1] != end[p2]: return False
            if start[p1] == "L" and p1 < p2: return False
            if start[p1] == "R" and p1 > p2: return False
            p1 += 1
            p2 += 1
            while p1 < len(start) and start[p1] == "_": p1 += 1
            while p2 < len(end) and end[p2] == "_": p2 += 1
        return p1 == p2      
# @lc code=end

