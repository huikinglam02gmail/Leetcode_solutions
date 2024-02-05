#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_table = [[] for i in range(26)]
        for i, c in enumerate(s):
            hash_table[ord(c) - ord('a')].append(i)
        candidates = []
        for i in range(26):
            if len(hash_table[i]) == 1: candidates.append(hash_table[i][0])
        candidates.sort()
        if not candidates: return -1 
        else: return candidates[0]
# @lc code=end

