#
# @lc app=leetcode id=2186 lang=python3
#
# [2186] Minimum Number of Steps to Make Two Strings Anagram II
#

# @lc code=start
class Solution:
    '''
    get occurrence frequency of s and t
    Add abs(s occur - t occur)
    '''
    def minSteps(self, s: str, t: str) -> int:
        sOccur = [0] * 26
        tOccur = [0] * 26
        for c in s: sOccur[ord(c) - ord('a')] += 1
        for c in t: tOccur[ord(c) - ord('a')] += 1
        result = 0
        for i in range(26): result += abs(sOccur[i] - tOccur[i])
        return result
# @lc code=end

