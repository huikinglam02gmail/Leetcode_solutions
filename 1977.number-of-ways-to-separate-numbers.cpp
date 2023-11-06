/*
 * @lc app=leetcode id=1977 lang=cpp
 *
 * [1977] Number of Ways to Separate Numbers
 */

// @lc code=start
#include <vector>
#include <algorithm>
#include <string>

using std::string;
using std::vector;

class Solution {
public:
    int numberOfCombinations(std::string num) {
        const long long MOD = (long long)1000000007;
        int n = num.length();
        vector<vector<int>> lcs = commonSubstringLengthTable(num);
        vector<vector<long long>> prefixSum(n, vector<long long>(n, 0));
        
        if (num[0] != '0') {
            for (int j = 0; j < n; j++) {
                prefixSum[0][j] = 1;
            }
        }
        
        for (int i = 1; i < n; i++) {
            for (int j = i; j < n; j++) {
                prefixSum[i][j] += prefixSum[i - 1][j];
                
                if (num[i] != '0') {
                    long long current = prefixSum[i - 1][i - 1];
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
        
        return static_cast<int>(prefixSum[n - 1][n - 1]);
    }
    
    vector<vector<int>> commonSubstringLengthTable(string s) {
        int n = s.length();
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
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
};

// @lc code=end

