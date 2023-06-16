#
# @lc app=leetcode id=1569 lang=python3
#
# [1569] Number of Ways to Reorder Array to Get Same BST
#

# @lc code=start
import math
from typing import List


class Solution:
    '''
    The root must be the first number in the array
    Then we know its left child must be the first smaller number than itself, and its right child must be the first larger element than itself
    So the problem can be broken down to
    if there are l elements smaller than itself and n - 1 - l elements larger than itself, i.e. sorted(arr) = [a1,...,al, arr[0], a(l+1)....an]
    Then we reduce to the problem of having n - 1 free cells and in there we are picking up l cells and display the cells in order.
    f(arr) = f(unsorted(arr[smaller]))*f(unsorted(arr[larger]))*(n-1)Cl
    basis case: if one element left: return 1
    At the end, return result - 1 because the current nums is not included
        
    '''

    def divideAndConquer(self, arr):
        if len(arr) < 2:
            return 1
        root, n = arr[0], len(arr)
        left, right = [], []
        for i in range(1, n):
            if arr[i] < root:
                left.append(arr[i])
            else:
                right.append(arr[i])
        nl = len(left)
        return ((math.comb(n-1, nl) % self.MOD) * self.divideAndConquer(left) * self.divideAndConquer(right)) % self.MOD
    
    def numOfWays(self, nums: List[int]) -> int:
        self.MOD = pow(10, 9) + 7
        return (self.divideAndConquer(nums) - 1) % self.MOD
# @lc code=end

