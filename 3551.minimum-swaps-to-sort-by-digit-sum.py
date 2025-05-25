#
# @lc app=leetcode id=3551 lang=python3
#
# [3551] Minimum Swaps to Sort by Digit Sum
#

# @lc code=start
from typing import List


class Solution:
    '''
    Sort the array by [digit sum, num, i] and find the cycle size of each index
    The number of swaps needed to sort the cycle is size - 1
    '''
    def digitSum(self, num: int) -> int:
        return sum(int(digit) for digit in str(num))
    
    def minSwaps(self, nums: List[int]) -> int:
        data = [[self.digitSum(num), num, i] for i, num in enumerate(nums)]
        data.sort()
        visited = [False] * len(nums)
        swaps = 0
        for i in range(len(nums)):
            if visited[i]: continue
            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = data[j][2]
                cycle_size += 1
            swaps += cycle_size - 1
        return swaps
        
# @lc code=end

