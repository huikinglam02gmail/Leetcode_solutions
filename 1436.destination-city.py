#
# @lc app=leetcode id=1436 lang=python3
#
# [1436] Destination City
#

# @lc code=start
class Solution:
    # Count outgoing edges
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing = {}
        for start, end in paths:
            if start not in outgoing:
                outgoing[start] = 0
            outgoing[start] += 1
            if end not in outgoing:
                outgoing[end] = 0
        
        for k, v in outgoing.items():
            if v == 0:
                return k
# @lc code=end

