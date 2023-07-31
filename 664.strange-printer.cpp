/*
 * @lc app=leetcode id=664 lang=cpp
 *
 * [664] Strange Printer
 */

// @lc code=start
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int strangePrinter(string s) {
        string str;
        for (char c : s) {
            if (str.empty() || c != str.back()) {
                str.push_back(c);
            }
        }
        
        int n = str.length();
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        for (int j = 0; j < n; j++) {
            for (int i = j; i >= 0; i--) {
                if (i == j) {
                    dp[i][j] = 1;
                } else if (i == j - 1) {
                    dp[i][j] = 2;
                } else {
                    dp[i][j] = 1 + dp[i + 1][j];
                    for (int k = i + 1; k <= j; k++) {
                        if (str[i] == str[k]) {
                            dp[i][j] = min(dp[i][j], dp[i + 1][k - 1] + dp[k][j]);
                        }
                    }
                }
            }
        }
        return dp[0][n - 1];
    }
};

// @lc code=end

