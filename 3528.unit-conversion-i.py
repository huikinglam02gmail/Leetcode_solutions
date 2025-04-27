#
# @lc app=leetcode id=3528 lang=python3
#
# [3528] Unit Conversion I
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        graph = [{} for i in range(len(conversions) + 1)]
        MOD = 1000000007
        for source, target, factor in conversions:
            graph[source][target] = factor
            graph[target][source] = - factor
        result = [0] * (len(conversions) + 1)
        result[0] = 1
        dq = deque()
        dq.append([0, 1])
        while dq:
            node, val = dq.popleft()
            for nxt in graph[node]:
                if result[nxt] == 0:
                    if graph[node][nxt] >= 0: result[nxt] = val * graph[node][nxt]
                    else: result[nxt] = val / (- graph[node][nxt])
                    result[nxt] %= MOD
                    dq.append([nxt, result[nxt]])
        return result
# @lc code=end

