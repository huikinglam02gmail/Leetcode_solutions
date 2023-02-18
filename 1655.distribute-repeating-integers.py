#
# @lc app=leetcode id=1655 lang=python3
#
# [1655] Distribute Repeating Integers
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    # There are only 10 customers and 50 types of nums
    # So we can use bitmask to use bitmask[ith bit] = 1 to represent customer[i] is satisfied
    # Then we can save all the possible configurations in which a certain bitmask is satisfied
    # Then we ask for if dp[2^m - 1] is true
    # To look for a possible solution, we backtrack: for each customer
    # we ration the appropriate amount to any ok customer, and further dfs into the  
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        self.hashTable =  Counter(nums)
        m = len(quantity)
        dp = [False for i in range(1 << m)]
        dp[0] = {}
        okSet = [[] for i in range(1 << m)]
        for i in range(1 << m):
            binI = bin(i)[2:]
            for j in range(len(binI)):
                if i & (1 << j) != 0:
                    
# @lc code=end

