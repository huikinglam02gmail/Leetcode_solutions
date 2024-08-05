#
# @lc app=leetcode id=2053 lang=python3
#
# [2053] Kth Distinct String in an Array
#

# @lc code=start
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hash_table = {}
        for c in arr: hash_table[c] = hash_table.get(c, 0) + 1
        counter = 0
        for i in arr:
            if hash_table[i] == 1:
                counter += 1
                if counter == k: return i
        return ""
# @lc code=end

