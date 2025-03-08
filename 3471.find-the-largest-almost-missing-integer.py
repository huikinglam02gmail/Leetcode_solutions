#
# @lc app=leetcode id=3471 lang=python3
#
# [3471] Find the Largest Almost Missing Integer
#

# @lc code=start
from typing import List


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        hashTable = {}
        for i in range(len(nums) - k + 1):
            seen = set()
            for j in range(i, i + k): seen.add(nums[j])
            for num in seen: hashTable[num] = hashTable.get(num, 0) + 1

        for k, v in sorted(hashTable.items(), key = lambda x: -x[0]):
            if v == 1: return k
        return -1
# @lc code=end

