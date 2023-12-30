#
# @lc app=leetcode id=1897 lang=python3
#
# [1897] Redistribute Characters to Make All Strings Equal
#

# @lc code=start
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        hash_table = [0] * 26
        for word in words:
            for c in word: hash_table[ord(c) - ord('a')] += 1
        for i in range(26):
            if hash_table[i] % len(words) != 0: 
                return False
        return True
    
    
    # @lc code=end

