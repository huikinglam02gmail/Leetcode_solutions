#
# @lc app=leetcode id=1519 lang=python3
#
# [1519] Number of Nodes in the Sub-Tree With the Same Label
#

# @lc code=start
from collections import deque


class Solution:
    # BFS from 0 and record parent of each node. Also, record (downward going) adjacency of each node
    # Then we start from nodes with 0 adjacency and move back up

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # Set up the graph
        graph = [set() for i in range(n)]
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        # BFS from 0, record parent and adjacency count of each node
        dq = deque()
        dq.append(0)
        parents = [-2]*n
        adjacency = [0]*n
        parents[0] = -1
        while dq:
            node = dq.popleft()
            for nxt in graph[node]:
                if parents[nxt] == -2: # nxt is unvisited
                    dq.append(nxt)
                    parents[nxt] = node
                    adjacency[node] += 1

        # poplulate the leaves and BFS back up
        dq = deque()
        for i in range(n):
            if adjacency[i] == 0:
                dq.append(i)
        
        # Dictionary of character count of each node subtree
        counts = [[0 for j in range(26)] for i in range(n)]
        result = [0]*n
        
        while dq:
            node = dq.popleft()
            counts[node][ord(labels[node]) - ord('a')] += 1
            result[node] = counts[node][ord(labels[node]) - ord('a')]
            if parents[node] >= 0:
                for j in range(26):
                    counts[parents[node]][j] += counts[node][j]
                adjacency[parents[node]] -= 1
                if adjacency[parents[node]] == 0:
                    dq.append(parents[node])
        return result
# @lc code=end

