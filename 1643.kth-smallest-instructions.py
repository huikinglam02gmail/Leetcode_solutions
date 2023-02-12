#
# @lc app=leetcode id=1643 lang=python3
#
# [1643] Kth Smallest Instructions
#

# @lc code=start
import math
from typing import List


class Solution:
    #  This is a math problem
    #  we know the answer must contain destination[0] V and destination[1] H
    #  and we know H is lexicographically smaller than V
    #  So we know there would be (V＋ Ｈ) C Ｖ = total number of combinations
    #  The first H/(V + H) * total  lexicographically smallest instruction start with H, and the rest start with V
    #  So we compare k with that
    #  and recursively call the same function
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        if destination[0] == 0:
            return 'H' * destination[1]
        if destination[1] == 0:
            return 'V' * destination[0]
        total = math.comb(sum(destination), destination[0])
        if k  <= total * destination[1] // sum(destination):
            return 'H' + self.kthSmallestPath([destination[0], destination[1] - 1], k)
        else:
            return 'V' + self.kthSmallestPath([destination[0] - 1, destination[1]], k - total * destination[1] // sum(destination))
        
# @lc code=end

