/*
 * @lc app=leetcode id=1977 lang=csharp
 *
 * [1977] Number of Ways to Separate Numbers
 */

// @lc code=start
public class Solution {
    public int NumberOfCombinations(string num) {
        const long MOD = 1000000007;
        int n = num.Length;
        int[][] lcs = CommonSubstringLengthTable(num);
        long[][] prefixSum = new long[n][];
        for (int i = 0; i < n; i++) {
            prefixSum[i] = new long[n];
        }
        
        if (num[0] != '0') {
            for (int j = 0; j < n; j++) {
                prefixSum[0][j] = 1;
            }
        }
        
        for (int i = 1; i < n; i++) {
            for (int j = i; j < n; j++) {
                prefixSum[i][j] += prefixSum[i - 1][j];
                
                if (num[i] != '0') {
                    long current = prefixSum[i - 1][i - 1];
                    int l = j - i + 1;
                    int prevStart = i - l;
                    
                    if (prevStart >= 0) {
                        current -= prefixSum[prevStart][i - 1];
                        current = (current + MOD) % MOD;
                        
                        if (lcs[prevStart][i] >= l || num[prevStart + lcs[prevStart][i]] < num[i + lcs[prevStart][i]]) {
                            current += prefixSum[prevStart][i - 1];
                            current %= MOD;
                            
                            if (prevStart > 0) {
                                current -= prefixSum[prevStart - 1][i - 1];
                                current = (current + MOD) % MOD;
                            }
                        }
                    }
                    
                    prefixSum[i][j] += current;
                    prefixSum[i][j] %= MOD;
                }
            }
        }
        
        return (int)prefixSum[n - 1][n - 1];
    }
    
    public int[][] CommonSubstringLengthTable(string s) {
        int n = s.Length;
        int[][] dp = new int[n][];
        
        for (int i = 0; i < n; i++) {
            dp[i] = new int[n];
        }
        
        dp[n - 1][n - 1] = 1;
        
        for (int i = n - 2; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (s[i] == s[j]) {
                    dp[i][j]++;
                    
                    if (j + 1 < n) {
                        dp[i][j] += dp[i + 1][j + 1];
                    }
                }
            }
        }
        
        return dp;
    }
}

// @lc code=end

