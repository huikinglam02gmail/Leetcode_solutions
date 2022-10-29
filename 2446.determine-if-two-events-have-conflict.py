#
# @lc app=leetcode id=2446 lang=python3
#
# [2446] Determine if Two Events Have Conflict
#

# @lc code=start
from typing import List
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        start1 = int(event1[0][:2])*60 + int(event1[0][3:])
        end1 = int(event1[1][:2])*60 + int(event1[1][3:])
        start2 = int(event2[0][:2])*60 + int(event2[0][3:])
        end2 = int(event2[1][:2])*60 + int(event2[1][3:])
        time = [[start1, end1], [start2, end2]]
        time.sort()
        return time[0][1] >= time[1][0]
        
# @lc code=end

