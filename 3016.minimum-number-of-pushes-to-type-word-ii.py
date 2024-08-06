#
# @lc app=leetcode id=3016 lang=python3
#
# [3016] Minimum Number of Pushes to Type Word II
#

# @lc code=start
class Solution:
    '''
    Allocate from highest to lowest occurrence
    '''
    def minimumPushes(self, word: str) -> int:
        counts = [0] * 26
        for c in word: counts[ord(c) - ord('a')] += 1
        result = 0
        counts.sort(reverse=True)
        for i, c in enumerate(counts): result += c * ((i // 8) + 1)
        return result
        
# @lc code=end

