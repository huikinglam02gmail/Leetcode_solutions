#
# @lc app=leetcode id=889 lang=python3
#
# [889] Construct Binary Tree from Preorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional


class Solution:
    '''
    preorder: root -> left -> right
    postorder: left -> right -> root
    For example: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
    We know at the first layer, the root must be 1 because it appears at the beginning of preorder and ending of postorder
    Then we need to decide where to cut out the left and right part of the branches
    We know that the value of the left subtree node must be 2 and the value of the right substree root must be 3 from the preorder and postorder 
    The next task is to find the cutting point: left_preorder = [2,4,5], right_preorder = [3,6,7]; left_postorder = [4,5,2], right_postorder = [6,7,3]
    Edge cases:
    preorder = [2,1,3], postorder = [3,1,2]
    We found that left_root_val, right_root_val are the same
    Therefore there are no right subtrees    
    '''

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        if len(preorder) > 2:
            left_root_val, right_root_val = preorder[1], postorder[-2]
            if left_root_val != right_root_val:
                preorder_cut = preorder.index(right_root_val)
                postorder_cut = postorder.index(left_root_val)
                root.left = self.constructFromPrePost(preorder[1:preorder_cut], postorder[:postorder_cut+1])
                root.right = self.constructFromPrePost(preorder[preorder_cut:], postorder[postorder_cut+1:-1])
            else:
                root.left = self.constructFromPrePost(preorder[1:], postorder[:-1])
        elif len(preorder) == 2:
            left_root_val = preorder[1]
            root.left = self.constructFromPrePost([preorder[1]], [postorder[0]])        
        return root
        
# @lc code=end

