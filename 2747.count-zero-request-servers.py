#
# @lc app=leetcode id=2747 lang=python3
#
# [2747] Count Zero Request Servers
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        queriesWithIndex = sorted((q, i) for i, q in enumerate(queries))
        logs.sort(key=lambda log: log[1])
        logIndex = 0
        result = [0] * len(queries)
        freeCount = n
        dq = deque()
        inDeque = {}
        for q, i in queriesWithIndex:
            while logIndex < len(logs) and logs[logIndex][1] < q - x: logIndex += 1
            while dq and dq[0][1] < q - x:
                serverId, time = dq.popleft()
                inDeque[serverId] -= 1
                if inDeque[serverId] == 0:
                    freeCount += 1
                    inDeque.pop(serverId)
            while logIndex < len(logs) and logs[logIndex][1] <= q:
                serverId, time = logs[logIndex]
                dq.append([serverId, time])
                if serverId not in inDeque:
                    inDeque[serverId] = 0
                    freeCount -= 1
                inDeque[serverId] += 1
                logIndex += 1
            result[i] = freeCount
        return result
# @lc code=end

