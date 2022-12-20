#
# @lc app=leetcode id=2509 lang=python3
#
# [2509] Cycle Length Queries in a Tree
#

# @lc code=start
class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        result = []
        for a, b in queries:
            aDict = {}
            aCount = 0
            while a != 0:
                aDict[a] = aCount
                aCount += 1
                a //= 2
            bCount = 0
            while b not in aDict:
                bCount += 1
                b //= 2
            result.append(1 + aDict[b] + bCount)
        return result
        
# @lc code=end

