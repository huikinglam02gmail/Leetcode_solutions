#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
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


from collections import deque
from typing import List, Optional


class Solution:
    '''
    Use a hash set to store the previously unseen nodes. As the root would never be a subtree, we should use postorder traversal to visit the tree, so that more simple tree structures are compared first. Each new node will be compared with all items in hash set and decide if it is a subtree. If not, add to the hash set. Tricky part in the algorithm: we need to serialize a subtree into string because we cannot handle that in the hash set.
   
    '''

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # Breadth-first search
        # include null nodes as well!
        dq = deque()
        dq.append(root)
        bfs = []
        while dq:
            node = dq.popleft()
            if node:
                bfs.append(str(node.val))
                dq.append(node.left)
                dq.append(node.right)
            else:
                bfs.append("null")
        return ','.join(bfs)
                
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode

        start with the first entry as root, then put each node into the queue. Use left or not left to define whether it is the left or right child currently pop from the queue when it is left        
        """

        if data == "null":
            return
        else:
            strings = data.split(",")
            root = TreeNode(int(strings[0]))
            dq = deque([root])
            left = True
            
            for string in strings[1:]:
                if string != "null":
                    node = TreeNode(int(string))
                    dq.append(node)
                else:
                    node = None
                if left:
                    parent = dq.popleft()
                    parent.left = node
                else:
                    parent.right = node
                left = not left
            return root
 
    def dfs(self, root):
        if root.left:
            self.dfs(root.left)
        if root.right:
            self.dfs(root.right)
        root_string = self.serialize(root)
        if root_string not in self.hash_set:
            self.hash_set.add(root_string)
        else:
            self.result.add(root_string)
    
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.hash_set = set()
        self.result = set()
        self.dfs(root)
        res = []
        for node_string in self.result:
            res.append(self.deserialize(node_string))
        return res
# @lc code=end

