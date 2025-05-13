#
# @lc app=leetcode id=3335 lang=python3
#
# [3335] Total Characters in String After Transformations I
#

# @lc code=start
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        counts = [0] * 26
        MOD = 1000000007
        for c in s: counts[ord(c) - ord('a')] += 1
        for i in range(t):
            countZ = counts[-1]
            for j in range(25, 0, -1): counts[j] = counts[j - 1]
            counts[0] = countZ
            counts[1] += countZ
            for j in range(26): counts[j] %= MOD
        return sum(counts) % MOD
                

# @lc code=end

