#
# @lc app=leetcode id=3403 lang=python3
#
# [3403] Find the Lexicographically Largest String From the Box I
#

# @lc code=start
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        counts = [set()] * 26
        for i, c in enumerate(word): counts[ord(c) - ord('a')].add(i)
        l = 25
        while l > 0 and len(counts[l]) == 0: l -= 1
        
# @lc code=end

