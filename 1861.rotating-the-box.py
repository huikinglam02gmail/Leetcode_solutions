#
# @lc app=leetcode id=1861 lang=python3
#
# [1861] Rotating the Box
#

# @lc code=start
from typing import List


class Solution:
    '''
    Simulate the process
    First rotate the box first
    Then use two pointers on each column to simulate the fall    
    '''
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        rotated_box = [["" for i in range(m)] for j in range(n)]
        
        for i in range(m):
            for j in range(n):
                rotated_box[j][m-1-i] = box[i][j]
        
        for j in range(m):
            bottom = n - 1
            for top in range(n - 1, -1 ,-1):
                if bottom >= 0:
                    if rotated_box[top][j] == "*": bottom = top - 1
                    elif rotated_box[bottom][j] != ".": bottom -= 1                
                    elif rotated_box[top][j] == "#":
                        rotated_box[bottom][j], rotated_box[top][j] = rotated_box[top][j], rotated_box[bottom][j]
                        bottom -= 1
        return rotated_box
# @lc code=end

