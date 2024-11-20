#
# @lc app=leetcode id=2516 lang=python3
#
# [2516] Take K of Each Character From Left and Right
#

# @lc code=start
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        counts = [0] * 3
        for c in s: counts[ord(c) -ord('a')] += 1
        for i in range(3):
            if counts[i] < k: return -1

        i = 0
        count2 = [0] * 3
        n = len(s)
        result = n
        for j in range(n):
            count2[ord(s[j]) - ord('a')] += 1
            while (count2[0] > counts[0] - k or count2[1] > counts[1] - k or count2[2] > counts[2] - k) and i <= j:
                count2[ord(s[i]) - ord('a')] -= 1
                i += 1
            result = min(result, n - (j - i + 1))
        return result
# @lc code=end

