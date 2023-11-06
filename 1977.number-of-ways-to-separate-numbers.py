#
# @lc app=leetcode id=1977 lang=python3
#
# [1977] Number of Ways to Separate Numbers
#

# @lc code=start
class Solution:
    '''
    This is a problem to be solved by DP.
    Let dp[i][j] = number of possible lists of integers that you could have written down to get string num[:j + 1] and num[i: j + 1] is the last word.
    Base case: dp[i][j] = 0 if num[i] = 0, else dp[0][j] = 1
    Recurrence relation: dp[i][j] = dp[i - 1][i - 1] + ... + dp[i - (j - i)][i - 1] (+ dp[i - (j - i + 1)][i - 1] if num[2 * i - j - 1 :i] <= num[i: j + 1])
    We need two further preparation: prefix sum of dp[:][j] and finally, longest common substring between any two indices
    '''
    def numberOfCombinations(self, num: str) -> int:
        MOD = pow(10, 9) + 7
        n = len(num)
        lcs = self.commonSubstringLengthTable(num)
        prefixSum = [[0 for j in range(n)] for i in range(n)]
        if num[0] != '0':
            for j in range(n): 
                prefixSum[0][j] = 1
        for i in range(1, n):
            for j in range(i, n):
                prefixSum[i][j] += prefixSum[i - 1][j]
                if num[i] != "0":
                    current, l = prefixSum[i - 1][i - 1], j - i + 1
                    prevStart = i - l
                    if prevStart >= 0:
                        current -= prefixSum[prevStart][i - 1]
                        current %= MOD
                        if lcs[prevStart][i] >= l or num[prevStart + lcs[prevStart][i]] < num[i + lcs[prevStart][i]]:
                            current += prefixSum[prevStart][i - 1]
                            current %= MOD
                            if prevStart > 0:
                                current -= prefixSum[prevStart - 1][i - 1]
                                current %= MOD
                    prefixSum[i][j] += current
                    prefixSum[i][j] %= MOD
        return prefixSum[n - 1][n - 1]

    '''
    Method to find the common length of substrings between s[i:] and s[j:] in the string s.
    '''
    def commonSubstringLengthTable(self, s):
        n = len(s)
        dp = [[0 for j in range(n)] for i in range(n)]
        dp[n - 1][n - 1] = 1
        for i in range(n - 2, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    dp[i][j] += 1
                    if j + 1 < n:
                        dp[i][j] += dp[i + 1][j + 1]
        return dp

# @lc code=end

