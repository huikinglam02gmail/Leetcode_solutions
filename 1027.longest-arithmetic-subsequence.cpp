/*
 * @lc app=leetcode id=1027 lang=cpp
 *
 * [1027] Longest Arithmetic Subsequence
 */

// @lc code=start
#include<vector>
#include<algorithm>
using std::max;
using std::vector;
class Solution {
private:
    int n;
    int res;
public:
    int longestArithSeqLength(vector<int>& A) {
        int res = 2, n = A.size();
        vector<vector<int>> dp(n, vector<int>(2000, 0));
        for (int i = 0; i < n; ++i)
            for (int j = i + 1; j < n; ++j)  {
                int d = A[j] - A[i] + 1000;
                dp[j][d] = max(2, dp[i][d] + 1);
                res = max(res, dp[j][d]);
            }
        return res;
    }
};
// @lc code=end
