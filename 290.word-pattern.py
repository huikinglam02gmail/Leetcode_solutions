#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    # split s
    # then 
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_split, hash_table = s.split(" "), {}
        if len(pattern) != len(s_split):
            return False
        seen = set()
        for i, c in enumerate(pattern):
            if c in hash_table and s_split[i] != hash_table[c]:
                return False
            elif c not in hash_table and s_split[i] in seen:
                return False
            else:
                hash_table[pattern[i]] = s_split[i]
                seen.add(s_split[i])
        return True
# @lc code=end

