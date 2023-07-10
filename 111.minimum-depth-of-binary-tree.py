#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        dq = deque()
        dq.append(root)
        steps = 1
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                if not node.left and not node.right:
                    return steps
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            steps += 1
        return -1

# @lc code=end

