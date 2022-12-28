#
# @lc app=leetcode id=1573 lang=python3
#
# [1573] Number of Ways to Split a String
#

# @lc code=start
class Solution:
    #  First go through s. Count number of ones
    # If it is not divisible by 3, return 0
    # Then the answer is quite simple: possible choice of start point of second fragment * that of 3rd segment. if the last 1 of first segment is at i, and the next 1 is j, we can start at i + 1,...., j for segment 2. Same for segment 3

    def numWays(self, s: str) -> int:
        counts, n, MOD = [], len(s), pow(10, 9) + 7
        for i, c in enumerate(s):
            if c == '1':
                counts.append(i)
        if (len(counts) % 3) != 0:
            return 0
        elif len(counts) == 0:
            result = 0
            for i in range(1, n - 1):
                result += (n - i - 1)
                result %= MOD
            return result
        else:
            l = len(counts) // 3
            return ((counts[l] - counts[l-1]) * (counts[2*l] - counts[2*l - 1])) % MOD
# @lc code=end
