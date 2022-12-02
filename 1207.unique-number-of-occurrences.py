#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_table = {}
        for num in arr:
            hash_table[num] = hash_table.get(num, 0) + 1
        freq = set()
        for value in list(hash_table.values()):
            if value not in freq:
                freq.add(value)
            else:
                return False
        return True
# @lc code=end

