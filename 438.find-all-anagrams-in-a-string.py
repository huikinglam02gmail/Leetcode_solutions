#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        if len(p) <= len(s):
            hash_p = [0]*26
            for c in p:
                hash_p[ord(c) - ord('a')] += 1
            hash_s = [0]*26
            for i in range(len(s)):
                hash_s[ord(s[i]) - ord('a')] += 1
                if i >= len(p):
                    hash_s[ord(s[i - len(p)]) - ord('a')] -= 1
                if all([hash_s[j] == hash_p[j] for j in range(26)]):
                    result.append(i - len(p) + 1)
        return result
        # @lc code=end

