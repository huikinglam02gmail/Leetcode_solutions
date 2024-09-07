#
# @lc app=leetcode id=1367 lang=python3
#
# [1367] Linked List in Binary Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    '''
    Can use a recursive function to achieve the goal
    if head.val == node.val, we can try to dfs from the current node
    Also we can try to dfs from its children
    Condition of the linked list is inside the tree: head == None    
    '''
    def dfs(self, head, node):
        if not head: return True
        if not node: return False
        return node.val == head.val and (self.dfs(head.next, node.left) or self.dfs(head.next, node.right))
    
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head: return True
        if not root: return False
        return self.dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
        
# @lc code=end

