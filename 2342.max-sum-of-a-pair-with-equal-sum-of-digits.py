#
# @lc app=leetcode id=2342 lang=python3
#
# [2342] Max Sum of a Pair With Equal Sum of Digits
#

# @lc code=start
from typing import List


class Solution:
    def sum_of_digits(self, num):
        num_string = str(num)
        result = 0
        for c in num_string: result += int(c)
        return result
    
    def maximumSum(self, nums: List[int]) -> int:
        hash_table = {}
        for num in nums:
            num_digit_sum = self.sum_of_digits(num)
            if num_digit_sum not in hash_table: hash_table[num_digit_sum] = []
            hash_table[num_digit_sum].append(num)
        
        keys = list(hash_table.keys())
        max_seen = - 1
        for key in keys:
            if len(hash_table[key]) > 1: max_seen = max(max_seen, sum(sorted(hash_table[key], reverse = True)[0:2]))
        return max_seen
# @lc code=end

