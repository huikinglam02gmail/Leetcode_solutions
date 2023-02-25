#
# @lc app=leetcode id=1675 lang=python3
#
# [1675] Minimize Deviation in Array
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    This is the same problem as 632.
    If num is odd, it can only be [num, 2*num]
    If num is even, it can be [num // (2^n), ... ,num // 2, num] in which num // (2^n) is odd
    '''
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        globalMax, globalMin, maxSoFar = - float('inf'), float('inf'), - float('inf')
        heap = []
        for i, num in enumerate(nums):
            globalMax = max(globalMax, num[-1])
            globalMin = min(globalMin, num[0])
            heapq.heappush(heap, [num[0], i, 0])
            maxSoFar = max(maxSoFar,num[0])
            
        result = [globalMin, globalMax]
        diff = globalMax - globalMin
        
        while heap:
            num, row, col = heapq.heappop(heap)
            if maxSoFar - num < diff:
                diff = maxSoFar - num
                result = [num, maxSoFar]
            if col < len(nums[row]) - 1:
                heapq.heappush(heap, [nums[row][col + 1], row, col + 1])
                maxSoFar = max(maxSoFar, nums[row][col + 1])
            else:
                break
        return result


    def minimumDeviation(self, nums: List[int]) -> int:
        data = []
        for num in nums:
            datum = []
            if num % 2 == 1:
                datum.append(num)
                datum.append(2 * num)
            else:
                temp = num
                while temp % 2 == 0:
                    datum.append(temp)
                    temp //= 2
                datum.append(temp)
                datum.reverse()
            data.append(datum)
        
        smallestR = self.smallestRange(data)
        return smallestR[1] - smallestR[0] 
        
# @lc code=end

