#
# @lc app=leetcode id=1558 lang=python3
#
# [1558] Minimum Numbers of Function Calls to Make Target Array
#

# @lc code=start
from typing import List


class Solution:
    # we can try to revert the line of thought: try to arrive at [0]*n
    # Firstly, we should note that elements with same value goes down together, with 1 step when it is even, with l steps when it is odd
    # The optimal path would be first convert all the elements to even and divide by 2 together
    def minOperations(self, nums: List[int]) -> int:
        dict1 = {}
        for num in nums:
            if num not in dict1:
                dict1[num] = 0
            dict1[num] += 1

        result = 0
        while dict1:
            dict2 = {}
            for key in dict1.keys():
                key2 = key
                if key2 & 1 > 0:
                    result += dict1[key]
                    key2 -= 1
                key2 //= 2
                if key2 > 0:
                    if key2 not in dict2:
                        dict2[key2] = 0
                    dict2[key2] += dict1[key]
            if dict2:
                result += 1
            dict1 = dict2
        return result
# @lc code=end

