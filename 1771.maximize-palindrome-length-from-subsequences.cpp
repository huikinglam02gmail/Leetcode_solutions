/*
 * @lc app=leetcode id=1771 lang=cpp
 *
 * [1771] Maximize Palindrome Length From Subsequences
 */

// @lc code=start
#include<string>
#include<vector>
#include<algorithm>
using std::max;
using std::string;
using std::vector;
class Solution {
public:
    int longestPalindrome(string word1, string word2) {
        string s = word1 + word2;
        int m = word1.size();
        vector<vector<int>> dp;
        dp.resize(s.size(), vector<int>(s.size(), 0));
        int result = 0;
        
        for (int j = 0; j < s.size(); j++)
        {
            for (int i = j; i >= 0; i--)
            {
                if (i == j)
                {
                    dp[i][j] = 1;
                }
                else
                {
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j]);
                    if (s[i] == s[j])
                    {
                        dp[i][j] = max(dp[i][j], 2 + dp[i + 1][j - 1]);
                        if (i < m && j >= m)
                        {
                            result = max(result, dp[i][j]);
                        }
                    }
                }
            }
        }
        
        return result;        
    }
};
// @lc code=end

