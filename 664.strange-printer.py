#
# @lc app=leetcode id=664 lang=python3
#
# [664] Strange Printer
#

# @lc code=start
class Solution:
    '''
    First remove repeating strings because they are not relevant
    Then DP:
    base case: single character will be 1
    two characters: will be always 2 in our case
    For the rest, an example is like this:
    bacdadacbdb
    when we calculate the dp for this, we see that if b is on the ends of the substring, any b inside the substring will benefit
    so the dp result would be dp[bacdadacbdb] = dp[acdadac] + dp[bdb]
    The base case without any repeat is dp[eacdadacbdb] = 1 + dp[acdadacbdb]              
    '''
    def strangePrinter(self, s: str) -> int:
        string = ""
        for c in s:
            if not string or c != string[-1]:
                string += c
        dp = [[0 for i in range(len(string))] for j in range(len(string))]
        for j in range(len(string)):
            for i in range(j,-1,-1):
                if i == j:
                    dp[i][j] = 1
                elif i == j - 1:
                    dp[i][j] = 2
                else:
                    dp[i][j] = 1 + dp[i+1][j]
                    for k in range(i + 1, j + 1):
                        if string[i] == string[k]:
                            dp[i][j] = min(dp[i][j], dp[i+1][k-1] + dp[k][j])
        return dp[0][len(string)-1]
# @lc code=end

