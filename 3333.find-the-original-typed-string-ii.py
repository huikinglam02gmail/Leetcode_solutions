#
# @lc app=leetcode id=3333 lang=python3
#
# [3333] Find the Original Typed String II
#

# @lc code=start
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        freqs = [1]
        MOD = 1000000007
        for i in range(1, len(word)):
            if word[i] == word[i - 1]: freqs[-1] += 1
            else: freqs.append(1)
        total = 1
        for freq in freqs:
            total *= freq
            total %= MOD
        if len(freqs) >= k: return total
        dp = [0] * k
        dp[0] = 1
        for freq in freqs:
            dpNew = [0] * k
            S = 0
            for i in range(1, k):
                S += dp[i - 1]
                S %= MOD
                if i > freq: 
                    S -= dp[i - freq - 1]
                    S += MOD
                    S %= MOD
                dpNew[i] = S
            dp = dpNew
        for ele in dp:
            total -= ele
            total += MOD
            total %= MOD
        return total
# @lc code=end

