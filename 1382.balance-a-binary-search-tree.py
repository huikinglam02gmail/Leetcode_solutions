#
# @lc app=leetcode id=1382 lang=python3
#
# [1382] Balance a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Apply Day–Stout–Warren algorithm
    Procedure:
    1. Convert the tree into a vine:
        a. dummy node: dummy.right = root
        b. if dummy.right.left: rightRotate(dummy.right)
        c. else: dummy = dummy.right        
    '''

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        # Perform rotation
        y.left = z
        z.right = T2
        return y
    
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        # Perform rotation
        y.right = z
        z.left = T3
        # Return the new root
        return y
        
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Convert to a vine
        dummy = TreeNode(- float('Inf'), None, root)
        temp = dummy
        count = 0
        while temp.right:
            if temp.right.left: temp.right = self.rightRotate(temp.right)
            else:
                temp = temp.right
                count += 1
        # Decide how many nodes are in the last row
        last_row = count
        m = 0
        row = 0
        while last_row >= pow(2,row):
            last_row -= pow(2,row)
            m += pow(2,row)
            row += 1
        # Take care of the last row nodes
        temp = dummy
        for i in range(last_row):
            if temp.right.right: temp.right = self.leftRotate(temp.right)
            temp = temp.right
        # Final balancing
        j = m // 2
        while j > 0:
            temp = dummy
            for i in range(j):
                if temp.right.right: temp.right = self.leftRotate(temp.right)
                temp = temp.right
            j //= 2
        return dummy.right
# @lc code=end

