#
# @lc app=leetcode id=2382 lang=python3
#
# [2382] Maximum Segment Sum After Removals
#

# @lc code=start
import heapq
from typing import List

class UnionFindSet:
    def __init__(self, n=0):
        self.parents = [i for i in range(n)]
        self.count = n

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            pMax, pMin = max(pu,pv), min(pu,pv)
            self.parents[pMax] = pMin
            self.count -= 1


class Solution:
    '''
    Solve the problem from back to front. Use union find to hold the segments
    Keep track of whether a number is inserted yet.
    If the left or right or both are linked to the inserted num and is inserted, we find the parent of the left or right or both and get the sum. Then we update the sum and put back into heap
    '''
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        heap = []
        inserted = [False for i in range(n)]
        segmentSumToParentMap = {}
        UF = UnionFindSet(n)
        for i in range(n - 1, -1, -1):
            while heap and (heap[0][1] not in segmentSumToParentMap or segmentSumToParentMap[heap[0][1]] != - heap[0][0]): heapq.heappop(heap)
            if not heap: result[i] = 0
            else: result[i] = - heap[0][0]
            j = removeQueries[i]
            leftIsInserted = j > 0 and inserted[j - 1]
            rightIsInserted = j < n - 1 and inserted[j + 1]
            if not leftIsInserted and not rightIsInserted:
                inserted[j] = True
                heapq.heappush(heap, [- nums[j], UF.find(j)])
                segmentSumToParentMap[UF.find(j)] = nums[j]
                continue
            if leftIsInserted:
                leftOldSum = segmentSumToParentMap[UF.find(j - 1)]
                rightOldSum = segmentSumToParentMap.get(UF.find(j), nums[j])
                UF.union(j - 1, j)
                segmentSumToParentMap[UF.find(j)] = leftOldSum + rightOldSum
                heapq.heappush(heap, [- leftOldSum - rightOldSum, UF.find(j)])
            if rightIsInserted:
                leftOldSum = segmentSumToParentMap.get(UF.find(j), nums[j])
                rightOldSum = segmentSumToParentMap[UF.find(j + 1)]
                UF.union(j, j + 1)
                segmentSumToParentMap[UF.find(j)] = leftOldSum + rightOldSum
                heapq.heappush(heap, [- leftOldSum - rightOldSum, UF.find(j)])
            inserted[j] = True
        return result
            
        
# @lc code=end

