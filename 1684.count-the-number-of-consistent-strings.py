#
# @lc app=leetcode id=1684 lang=python3
#
# [1684] Count the Number of Consistent Strings
#

# @lc code=start
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = 0
        present = [0] * 26
        for c in allowed: present[ord(c) - ord('a')] += 1
        for word in words:
            for i in range(len(word)): 
                if not present[ord(word[i]) - ord('a')]: break
                elif i == len(word) - 1: result += 1
        return result
# @lc code=end

