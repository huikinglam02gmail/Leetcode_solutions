#
# @lc app=leetcode id=1462 lang=python3
#
# [1462] Course Schedule IV
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    2 <= numCourses <= 100
    0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)
    Union find would not work because it would not tell the prerequisite order
    As 1 <= queries.length <= 10^4, we want to avoid DFS for every query
    On the other hand, we are interested in the topological order of the prequisite tree
    For example, we can first construct the directed graph from i to j
    Then each i, BFS from it
    Construct the topological order for the sequence
    Then each query, we simply report Reachable[i][j]    
    '''

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [set() for i in range(numCourses)]
        for start, end in prerequisites: graph[start].add(end)
        data = [[i, q[0], q[1]] for i, q in enumerate(queries)]
        data.sort(key = lambda x: x[1])
        result = [False for i in range(len(queries))]
        last = -1
        visited = set()
        for i, a, b in data:
            if a != last:
                dq = deque()
                visited.clear()
                dq.append(a)
                visited.add(a)
                while dq:
                    node = dq.popleft()
                    for nxt in graph[node]:
                        if nxt not in visited:
                            dq.append(nxt)
                            visited.add(nxt)
                last = a
            result[i] = b in visited
        return result

# @lc code=end

