#
# @lc app=leetcode id=1028 lang=python3
#
# [1028] Recover a Tree From Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    '''
    preorder = root -> left -> right
    Then the task at hand is to look for "digit"+ -"+ "digit" in string
    Assign the first appearance to the left tree, the second to right
    We need to shorten - streaks by one in the resultant string    
    '''        
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        if len(traversal) == 0: return None
        currentNodeVal = 0
        i = 0
        while i < len(traversal) and traversal[i].isdigit():
            currentNodeVal *= 10
            currentNodeVal += int(traversal[i])
            i += 1
        node = TreeNode(currentNodeVal)
        nextStrings = ["", ""]
        if i < len(traversal):
            countDash = 0
            addToIndex =  0
            for j in range(i, len(traversal)):
                if traversal[j].isdigit() and countDash == 1 and len(nextStrings[0]) > 0: addToIndex += 1
                if traversal[j] == "-": countDash += 1
                else: countDash = 0
                if traversal[j].isdigit() or countDash > 1: nextStrings[addToIndex] += traversal[j]
        if nextStrings[0]: node.left = self.recoverFromPreorder(nextStrings[0])
        if nextStrings[1]: node.right = self.recoverFromPreorder(nextStrings[1])
        return node
    
# @lc code=end

