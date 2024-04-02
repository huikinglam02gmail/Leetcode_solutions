#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_table = {}
        seen = set()
        for i in range(len(s)):
            if ((s[i] not in hash_table and t[i] in seen) or (s[i] in hash_table and t[i] != hash_table[s[i]])): return False
            hash_table[s[i]] = t[i]
            seen.add(t[i])            
        return True
# @lc code=end

