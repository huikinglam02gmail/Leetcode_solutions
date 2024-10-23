#
# @lc app=leetcode id=2641 lang=python3
#
# [2641] Cousins in Binary Tree II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional


class Solution:
    '''
    To get at each level of cousins, we use BFS
    We need to label what group in nodes of same groups are non-cousins
    In a separate array, store the prefix Sums
    '''
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dq = deque()
        dq.append([root, 0])
        groups = [0]
        groupSum = [root.val]
        S = root.val
        while dq:
            groups2 = []
            groupid = 0
            groupSum2 = []
            S2 = 0
            for i in range(len(dq)):
                node, ind = dq.popleft()
                node.val = S - groupSum[ind]
                groupSum2.append(0)
                if node.left:
                    groups2.append(groupid)
                    groupSum2[-1] += node.left.val
                    S2 += node.left.val
                    dq.append([node.left, groupid])
                if node.right:
                    groups2.append(groupid)
                    groupSum2[-1] += node.right.val
                    S2 += node.right.val
                    dq.append([node.right, groupid])
                groupid += 1
            S = S2
            groupSum = groupSum2
            groups = groups2
        return root
# @lc code=end

