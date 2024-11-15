#
# @lc app=leetcode id=1574 lang=python3
#
# [1574] Shortest Subarray to be Removed to Make Array Sorted
#

# @lc code=start
import bisect
from typing import List


class Solution:
    '''
    3 cases:     
    1. chop from start
    2. chop from end
    3. chop from the middle
    Find the option which chop the least and return    
    '''
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        leftSubarray = [arr[0]]
        rightSubarray = [arr[-1]]
        
        p = 0
        while p < n - 1 and arr[p] <= arr[p + 1]:
            p += 1
            leftSubarray.append(arr[p])
        left = n - p - 1
        
        if left == 0: return 0

        p = n - 1
        while p > 0 and arr[p - 1] <= arr[p]:
            p -= 1
            rightSubarray.append(arr[p])
        right = p

        rightCorrect = []
        while rightSubarray: rightCorrect.append(rightSubarray.pop())
        
        nl, nr = len(leftSubarray), len(rightCorrect)
        mid = n
        for i in range(nl):
            ind = bisect.bisect_left(rightCorrect, leftSubarray[i])
            mid = min(mid, n - (i + 1) - (nr - ind))
        return min(mid, left, right)
            
# @lc code=end

