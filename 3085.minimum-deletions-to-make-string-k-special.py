#
# @lc app=leetcode id=3085 lang=python3
#
# [3085] Minimum Deletions to Make String K-Special
#

# @lc code=start
class Solution:
    '''
    First count all occurrences.
    For each character c, assume it is a part of the k special string, and its occurrence is the minimum occurrence among all characters.
    Then, for each other characters c1:
    1. If its occurrence is less than the minimum occurrence, we can delete all occurrences of it.
    2. If its occurrence is greater than the minimum occurrence + k, we can delete occur[c1] - (occur[c] + k) occurrences of it.
    '''
    def minimumDeletions(self, word: str, k: int) -> int:
        counts = [0] * 26
        for c in word: counts[ord(c) - ord('a')] += 1
        result = len(word)
        for i in range(26):
            current = 0
            for j in range(26):
                if counts[j] < counts[i]: current += counts[j]
                elif counts[j] > counts[i] + k: current += counts[j] - (counts[i] + k)
            result = min(result, current)
        return result
# @lc code=end

