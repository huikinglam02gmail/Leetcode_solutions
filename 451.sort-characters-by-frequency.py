#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        hash_table = {}
        for c in s: hash_table[c] = 1 + hash_table.get(c, 0)
        frequencies = sorted([[k, v] for k, v in list(hash_table.items())], key = lambda x: -x[1])
        result = ""
        for key, value in frequencies: result += key * value
        return result
# @lc code=end

