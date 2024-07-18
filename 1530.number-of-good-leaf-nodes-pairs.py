#
# @lc app=leetcode id=1530 lang=python3
#
# [1530] Number of Good Leaf Nodes Pairs
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    '''
     # The number of nodes in the tree is in the range [1, 210].
    # 1 <= Node.val <= 100
    # 1 <= distance <= 10
    # As node values might not be unique, we instead should use the binary tree node ID to denote different nodes
    # Because distance is quite limited, we can BFS from different leaves and report when we see other leaves    
    '''

    def countPairs(self, root: TreeNode, distance: int) -> int:
        dq = deque()
        dq.append((root, 0))
        leaves = set()
        graph = {}
        while dq:
            node, ind = dq.popleft()
            if not node.left and not node.right:
                leaves.add(ind)
            if ind not in graph:
                graph[ind] = set()
            if node.left:
                j = 2*ind + 1
                graph[ind].add(j)
                graph[j] = set()
                graph[j].add(ind)
                dq.append((node.left, j))
            if node.right:
                j = 2*ind + 2
                graph[ind].add(j)
                graph[j] = set()
                graph[j].add(ind)
                dq.append((node.right, j))
        
        result = 0
        for leaf in leaves:
            dq = deque()
            visited = set()
            dq.append(leaf)
            visited.add(leaf)
            steps = 0
            while steps <= distance and dq:
                for i in range(len(dq)):
                    node = dq.popleft()
                    if node != leaf and node in leaves:
                        result += 1
                    for nxt in graph[node]:
                        if nxt not in visited:
                            dq.append(nxt)
                            visited.add(nxt)
                steps += 1
        return result // 2
# @lc code=end

