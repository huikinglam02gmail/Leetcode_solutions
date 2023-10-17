#
# @lc app=leetcode id=1361 lang=python3
#
# [1361] Validate Binary Tree Nodes
#

# @lc code=start
from typing import List


class Solution:
    '''
    Valid binary tree:
    Each node can only has 1 parent
    Each node's child cannot be its parent
    Just perform union find        
    '''
    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        self.parent = [i for i in range(n)]
        for run in range(2):
            if run == 0:
                data = leftChild
            else:
                data = rightChild
            for i, child in enumerate(data):
                if child >= 0:
                    f_i, f_c = self.find(i), self.find(child)
                    if f_i == f_c:
                        return False
                    self.parent[child] = f_i
        return sum([x == i for i, x in enumerate(self.parent)]) == 1
# @lc code=end

