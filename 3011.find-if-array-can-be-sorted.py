#
# @lc app=leetcode id=3011 lang=python3
#
# [3011] Find if Array Can Be Sorted
#

# @lc code=start
from typing import List


class Solution:
    '''
    For all number, find # of set bits
    If the # of set bits in nums[i] == # of set bits in nums[i - 1], append to the last array
    Otherwise start a new Array
    Sort all the arrays
    Ask if the whole reconstructed array is sorted
    '''
    def canSortArray(self, nums: List[int]) -> bool:
        data = []
        setBits = []
        for i in range(1 << 8): setBits.append(bin(i + 1)[2:].count('1'))
        for i in range(len(nums)):
            if i > 0 and setBits[data[-1][-1] - 1] == setBits[nums[i] - 1]: data[-1].append(nums[i])
            else: data.append([nums[i]])
        for datum in data: datum.sort()
        i = 0
        j = 0
        last = -1
        while i < len(data) and j < len(data[i]):
            if data[i][j] < last: return False
            else:
                last = data[i][j]
                j += 1
                if j == len(data[i]):
                    j = 0
                    i += 1
        return True
# @lc code=end

