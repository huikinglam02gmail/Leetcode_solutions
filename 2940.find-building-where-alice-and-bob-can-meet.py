#
# @lc app=leetcode id=2940 lang=python3
#
# [2940] Find Building Where Alice and Bob Can Meet
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    In queries, 
    1. for i == j, ans = j
    2. for i < j:
        a. if heights[i] < heights[j]: ans = j
        b. ans > j, where heights[ans] > heights[i], if ans < len(heights)
    We put the queries to be solved in the min Heap queryHeap: [later occurring index, minimum Height to be considered, query index]
    Finally, we go through each height, check if it can solve the previously existing queries to be solved and keep putting in new elements to be considered from the heap. 
    '''
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ans = [-1] * len(queries)
        queryHeap = []
        for i, q in enumerate(queries):
            if q[0] == q[1]: ans[i] = q[0]
            elif q[0] < q[1]:
                if heights[q[0]] < heights[q[1]]: ans[i] = q[1]
                else: heapq.heappush(queryHeap, [q[1], heights[q[0]], i])
            else:
                if heights[q[1]] < heights[q[0]]: ans[i] = q[0]
                else: heapq.heappush(queryHeap, [q[0], heights[q[1]], i])
        heightHeap = []
        for i in range(len(heights)):
            while heightHeap and heightHeap[0][0] < heights[i]: ans[heapq.heappop(heightHeap)[1]] = i
            while queryHeap and queryHeap[0][0] <= i: 
                ind, Height, qInd = heapq.heappop(queryHeap)
                heapq.heappush(heightHeap, [Height, qInd])
        return ans
# @lc code=end

