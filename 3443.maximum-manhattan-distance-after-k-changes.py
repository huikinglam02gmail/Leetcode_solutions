#
# @lc app=leetcode id=3443 lang=python3
#
# [3443] Maximum Manhattan Distance After K Changes
#

# @lc code=start
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        counts = [0] * 2
        result = 0
        for i, c in enumerate(s):
            if c == 'N': counts[0] += 1
            elif c == "W": counts[1] += 1
            elif c == "S": counts[0] -= 1
            else: counts[1] -= 1
            result = max(result, min(abs(counts[0]) + abs(counts[1]) + 2 * k, i + 1))
        return result
# @lc code=end

