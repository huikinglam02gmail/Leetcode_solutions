#
# @lc app=leetcode id=786 lang=python3
#
# [786] K-th Smallest Prime Fraction
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    We have solved Leetcode 378. Kth Smallest Element in a Sorted Matrix before
    In here why don't we try to reduce the problem to exactly that?
    The idea is simple. matrix[i][j] = arr[i] / arr[j]
    All the elements are 1    
    '''
    def kthSmallest(self, matrix, k: int) -> int:
        heap = []
        order = [0 for i in range(len(matrix[0]))]
        for i in range(len(matrix[0])):
            heapq.heappush(heap, [matrix[0][i][1] / matrix[0][i][0], i])
        for i in range(k):
            x = heapq.heappop(heap)
            order[x[1]] += 1
            if order[x[1]] < len(matrix):
                heapq.heappush(heap, [matrix[order[x[1]]][x[1]][1] / matrix[order[x[1]]][x[1]][0], x[1]])
        return [self.arr[order[x[1]]-1], self.arr[x[1]]]
    
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        self.arr = arr
        matrix = [[[arr[i], arr[j]] for i in range(len(arr))] for j in range(len(arr))]
        return self.kthSmallest(matrix,k)
# @lc code=end

