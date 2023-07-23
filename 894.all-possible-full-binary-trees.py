#
# @lc app=leetcode id=894 lang=python3
#
# [894] All Possible Full Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional


class Solution:
    '''
    if n is even, it's just impossible
    if n is odd, we can use dynamic programming to solve:
    a FBT with n nodes must be a node with children being 1 + (n-2) or (n-2) + 1, add odd pairs upwards    
    '''

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        result = [[] for i in range(n+1)]
        for i in range(n+1):
            if i == 1:
                result[i].append(TreeNode(0))
            elif i % 2 == 1:
                for j in range(1, i, 2):
                    for k in range(len(result[j])):
                        for l in range(len(result[i-j-1])):
                            root = TreeNode(0)
                            root.left = result[j][k]
                            root.right = result[i-j-1][l]
                            result[i].append(root)
        return result[n]
# @lc code=end

