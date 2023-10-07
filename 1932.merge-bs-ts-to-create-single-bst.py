#
# @lc app=leetcode id=1932 lang=python3
#
# [1932] Merge BSTs to Create Single BST
#

# @lc code=start
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
    Key points to notice:
    No two roots of trees have the same value.
    To construct a final tree, there should be one root which never show up as leaf, and we start building from there.
    So first traverse through trees and record hashTable[root value] = index
    Also put all the root values into a set.
    Then traverse through trees again and loop through all leaves. If leaf value can be found inside the set, we discard that value from the set.
    If len(remaining set) != 1, we can return []
    Else: we build from trees[hashTable[setRemain]]. We put its left and right leaves in a queue for further build the tree. In the process, we record the previous smaller and larger number (the root). Then we pop from the queue, and find if the leaf value exist in the hashTable (There should only be one or none). Main check is if the root has a left child, we need to check if the prev smaller number of current leaf is smaller than the root's left children. Same for the right leaf. If passes, remove the root from the hashTable dictionary,and push its children into the queue
    '''
    
    def leafValInHashTable(self, node):
        if node.left:
            self.leafValInHashTable(node.left)
        if node.right:
            self.leafValInHashTable(node.right)
        if not node.left and not node.right and node.val in self.rootValSet:
            self.rootValSet.remove(node.val)

    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        if len(trees) == 1:
            return trees[0]
        hashTable = {}
        self.rootValSet = set()
        for i, tree in enumerate(trees):
            hashTable[tree.val] = i
            self.rootValSet.add(tree.val)
        
        for tree in trees:
            self.leafValInHashTable(tree)
        
        if len(self.rootValSet) == 1:
            for nodeVal in self.rootValSet:
                rootVal = nodeVal
            root = trees[hashTable[rootVal]]
            dq = deque()
            dq.append([root, None, None, 0, 50001])
            while dq:
                node, leftParent, rightParent, minimum, maximum = dq.popleft()
                if node.left:
                    dq.append([node.left, None, node, minimum, node.val])
                if node.right:
                    dq.append([node.right, node, None, node.val, maximum])
                if not node.left and not node.right and node.val in hashTable:
                    candidate = trees[hashTable[node.val]]
                    if candidate.right and candidate.right.val >= maximum:
                        continue
                    if candidate.left and candidate.left.val <= minimum:
                        continue                    
                    if leftParent:
                        leftParent.right = candidate
                        dq.append([candidate, leftParent, None, leftParent.val, maximum])
                    if rightParent:
                        rightParent.left = candidate
                        dq.append([candidate, None, rightParent, minimum, rightParent.val])
                    hashTable.pop(node.val)

            if len(hashTable) == 1:
                for k, v in hashTable.items():
                    root = v
                return trees[root]
        return None

# @lc code=end

