#
# @lc app=leetcode id=2176 lang=python3
#
# [2176] Count Equal and Divisible Pairs in an Array
#

# @lc code=start
from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        hash_table = {}
        for i in range(len(nums)):
            if nums[i] not in hash_table:
                hash_table[nums[i]] = [i]
            else:
                hash_table[nums[i]].append(i)
        result = 0
        for item in hash_table.values():
            if len(item) > 1:
                for i in range(len(item)-1):
                    for j in range(i+1,len(item),1):
                        if item[i]*item[j] % k == 0:
                            result += 1
        return result
        
# @lc code=end

