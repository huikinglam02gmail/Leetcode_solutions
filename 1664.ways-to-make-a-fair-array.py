#
# @lc app=leetcode id=1664 lang=python3
#
# [1664] Ways to Make a Fair Array
#

# @lc code=start
from typing import List


class Solution:
    '''
    We can first construct the prefix sum arrays of odd and even indices in nums. For each trial, removing a certain index means interchanging even and odd indices after it.
    Take the array [1, 2, 3, 4, 5] as an example. First we construct the prefix sum arrays prefixEven = [0, 1, 4, 9] and prefixOdd = [0, 2, 6]
    If we want to delete an odd index arr[i = 1] = 2, the 
    '''
    def waysToMakeFair(self, nums: List[int]) -> int:
        prefixOdd = [0]
        prefixEven = [0]
        for i, num in enumerate(nums):
            if i % 2 == 0:
                prefixEven.append(prefixEven[-1] + num)
            else:
                prefixOdd.append(prefixOdd[-1] + num)
        
# @lc code=end

