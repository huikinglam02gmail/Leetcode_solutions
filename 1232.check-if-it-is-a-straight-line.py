#
# @lc app=leetcode id=1232 lang=python3
#
# [1232] Check If It Is a Straight Line
#

# @lc code=start
from typing import List


class Solution:
    '''
    Check for cross product between two neighboring pairs    
    '''
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        for i in range(1, len(coordinates)-1):
            if  (coordinates[i][0] - coordinates[i-1][0])*(coordinates[i+1][1] - coordinates[i][1]) != (coordinates[i][1] - coordinates[i-1][1])*(coordinates[i+1][0] - coordinates[i][0]):
                return False
        return True
# @lc code=end

