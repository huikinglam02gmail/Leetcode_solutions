#
# @lc app=leetcode id=3258 lang=python3
#
# [3258] Count Substrings That Satisfy K-Constraint I
#

# @lc code=start
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        counts = [0, 0]
        left = 0
        result = 0
        for right in range(len(s)):
            if s[right] == "0": counts[0] += 1
            else: counts[1] += 1
            while counts[0] > k and counts[1] > k:
                if s[left] == "0": counts[0] -= 1
                else: counts[1] -= 1
                left += 1
            result += right - left + 1
        return result
# @lc code=end

