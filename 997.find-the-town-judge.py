#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
from typing import List


class Solution:
    # Just follow the instruction, be careful of the edge cases
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            if n == 1:
                return n
        else:
            hash_source = set()
            hash_sink = {}
            for item in trust:
                hash_source.add(item[0])
                if item[1] not in hash_sink:
                    hash_sink[item[1]] = 0
                hash_sink[item[1]] += 1
            for i in range(1,n+1):
                if i not in hash_source and i in hash_sink and hash_sink[i] == n-1:
                    return i
        return -1
# @lc code=end

