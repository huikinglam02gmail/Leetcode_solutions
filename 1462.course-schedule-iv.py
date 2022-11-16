#
# @lc app=leetcode id=1462 lang=python3
#
# [1462] Course Schedule IV
#

# @lc code=start
from collections import deque


class Solution:
    # 2 <= numCourses <= 100
    # 0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)
    # Union find would not work because it would not tell the prerequisite order
    # As 1 <= queries.length <= 10^4, we want to avoid DFS for every query
    # On the other hand, we are interested in the topological order of the prequisite tree
    # For example, we can first construct the directed graph from i to j
    # Then each i, BFS from it
    # Construct the topological order for the sequence
    # Then each query, we simply report Reachable[i][j]
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        Reachable = [[False for i in range(numCourses)] for j in range(numCourses)]
        graph = [set() for i in range(numCourses)]
        children = [set() for i in range(numCourses)]
        for start, end in prerequisites:
            graph[start].add(end)
        for i in range(numCourses):
            dq, visited = deque(), set()
            dq.append(i)
            visited.add(i)
            while dq:
                node = dq.popleft()
                for nxt in graph[node]:
                    if nxt > i and nxt not in visited:
                        dq.append(nxt)
                        visited.add(nxt)
                    elif not Reachable[i][nxt]: 
                        for item in children[nxt]:
                            Reachable[i][item] = True
                            children[i].add(item)
                    Reachable[i][nxt] = True
                    children[i].add(nxt)        
        
        result = []
        for start, end in queries:
            result.append(Reachable[start][end])
        return result
# @lc code=end

