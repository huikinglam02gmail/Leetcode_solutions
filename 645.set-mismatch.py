#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#

# @lc code=start
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hash_set, n, result, total = set(), len(nums), [], 0
        for num in nums:
            if num not in hash_set:
                hash_set.add(num)
                total += num
            else:
                result.append(num)
        result.append(n * (n + 1) // 2 - total)
        return result
# @lc code=end

