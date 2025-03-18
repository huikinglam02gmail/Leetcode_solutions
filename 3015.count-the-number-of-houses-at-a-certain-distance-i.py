#
# @lc app=leetcode id=3015 lang=python3
#
# [3015] Count the Number of Houses at a Certain Distance I
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        graph = [set() for i in range(n)]
        for i in range(n - 1):
            graph[i].add(i + 1)
            graph[i + 1].add(i)
        if x != y:
            graph[x - 1].add(y - 1)
            graph[y - 1].add(x - 1)
        
        result = [0 for i in range(n)]
        for i in range(n):
            dq = deque()
            visited = [False for j in range(n)]
            dq.append(i)
            visited[i] = True
            steps = 0
            while dq:
                for j in range(len(dq)):
                    node = dq.popleft()
                    for nxt in graph[node]:
                        if not visited[nxt]:
                            dq.append(nxt)
                            visited[nxt] = True
                result[steps] += len(dq)
                steps += 1
        return result
# @lc code=end

