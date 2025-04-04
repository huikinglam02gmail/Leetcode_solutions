#
# @lc app=leetcode id=3295 lang=python3
#
# [3295] Report Spam Message
#

# @lc code=start
from typing import List


class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        bannedWords = set(bannedWords)
        count = 0
        for word in message:
            if word in bannedWords: count += 1
            if count >= 2: return True
        return False
# @lc code=end

