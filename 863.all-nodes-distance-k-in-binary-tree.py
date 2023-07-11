#
# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    Build a graph from the tree. Then BFS from target
    '''
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = {}
        dq = deque()
        dq.append(root)
        graph[root.val] = set()
        while dq:
            node = dq.popleft()
            if node.left:
                graph[node.left.val] = set()
                graph[node.val].add(node.left.val)
                graph[node.left.val].add(node.val)
                dq.append(node.left)
            if node.right:
                graph[node.right.val] = set()                
                graph[node.val].add(node.right.val)
                graph[node.right.val].add(node.val)
                dq.append(node.right)
        
        dq = deque()
        visited = set()
        dq.append(target.val)
        visited.add(target.val)
        steps, result = 0, []
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                if steps == k:
                    result.append(node)
                else:
                    for nxt in graph[node]:
                        if nxt not in visited:
                            visited.add(nxt)
                            dq.append(nxt)
            if steps == k:
                return result
            else:
                steps += 1
        return result
# @lc code=end

