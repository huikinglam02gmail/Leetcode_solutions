#
# @lc app=leetcode id=1764 lang=python3
#
# [1764] Form Array by Concatenating Subarrays of Another Array
#

# @lc code=start
from typing import List


class Solution:
    '''
    if i > 0, the (i-1)th subarray appears before the ith subarray in nums. So we must find 0th first before finding 1st
    -107 <= groups[i][j], nums[k] <= 107
    groups.length == n
    1 <= n <= 10^3
    1 <= groups[i].length, sum(groups[i].length) <= 10^3
    1 <= nums.length <= 10^3
    Each number is at most 9 digits (sign + digits) and we have at most 1000 numbers, so to represent the whole string, at most 9000 digits + 1000 separators ~ 10000 characters long, okay for string matching
    So the strategy to serialize each group and nums into strings, and find occurrence of each group from nums. Specifically, we first look for groups[0] in nums[0:]. Suppose we find it at at index i. Then we look for group[i] in nums[i + len(group[0]):], so on
    '''
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        groupString = ["_" + "_".join(str(num) for num in group) for group in groups]
        numsString = "_" + "_".join(str(num) for num in nums)
        i, j = 0, 0
        while i < len(numsString) and j < len(groupString):
            ind = numsString.find(groupString[j], i)
            if ind == -1:
                return False
            else:
                i = ind + len(groupString[j])
                j += 1
        return j == len(groupString)
# @lc code=end
