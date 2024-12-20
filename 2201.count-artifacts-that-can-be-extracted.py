#
# @lc app=leetcode id=2201 lang=python3
#
# [2201] Count Artifacts That Can Be Extracted
#

# @lc code=start
from typing import List


class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        toDig = [set() for i in range(len(artifacts))]
        mapping = [[-1 for j in range(n)] for i in range(n)]
        for i, artifact in enumerate(artifacts):
            for r in range(artifact[0], artifact[2] + 1):
                for c in range(artifact[1], artifact[3] + 1):
                    toDig[i].add((r, c))
                    mapping[r][c] = i
        
        result = 0
        for x, y in dig:
            if mapping[x][y] != -1:
                toDig[mapping[x][y]].remove((x, y))
                if len(toDig[mapping[x][y]]) == 0: result += 1
                mapping[x][y] = -1
        return result
# @lc code=end
