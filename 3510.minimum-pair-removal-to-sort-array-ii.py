#
# @lc app=leetcode id=3510 lang=python3
#
# [3510] Minimum Pair Removal to Sort Array II
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    Keep a prev and a next array to specify the previous and next adjacent index like in a double linked list
    Keep a min heap saving [sum, index]
    Finally, keep a count of inverted adjacent elements
    Keep track of which nodes are deleted
    Simulate
    '''
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        prev = [-1] * n
        next = [n] * n 
        heap = []
        inverted = 0
        deleted = [False] * n
        for i in range(n):
            if i > 0: prev[i] = i - 1
            if i < n - 1: 
                next[i] = i + 1
                if nums[i] > nums[i + 1]: inverted += 1
                heapq.heappush(heap, [nums[i] + nums[i + 1], i])
        
        operations = 0
        while inverted > 0 and heap:
            while heap and (deleted[heap[0][1]] or next[heap[0][1]] == n or nums[heap[0][1]] + nums[next[heap[0][1]]] != heap[0][0]): heapq.heappop(heap)
            if heap:
                S, index = heapq.heappop(heap)
                operations += 1
                a = - float("inf")
                d = float("inf")
                b, c = nums[index], nums[next[index]]
                if prev[index] >= 0: a = nums[prev[index]]
                if next[next[index]] < n: 
                    d = nums[next[next[index]]]
                    prev[next[next[index]]] = index
                deleted[next[index]] = True
                next[index] = next[next[index]]     
                if prev[index] >= 0:  heapq.heappush(heap, [a + S, prev[index]])
                nums[index] = S
                if next[index] < n: heapq.heappush(heap, [S + d, index])
                if b < a <= b + c: inverted -= 1
                if b + c < a <= b: inverted += 1
                if b + c <= d < c: inverted -= 1
                if c <= d < b + c: inverted += 1
                if b > c: inverted -= 1
        return operations
            

# @lc code=end
