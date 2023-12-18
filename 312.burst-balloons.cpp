/*
 * @lc app=leetcode id=312 lang=cpp
 *
 * [312] Burst Balloons
 */

// @lc code=start
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int N = nums.size();
        vector<int> extendedNums(N + 2);
        copy(nums.begin(), nums.end(), extendedNums.begin() + 1);
        extendedNums[0] = 1;
        extendedNums[N + 1] = 1;

        vector<vector<int>> dp(N + 2, vector<int>(N + 2, 0));

        for (int j = 1; j <= N; j++) {
            dp[j][j] = extendedNums[j - 1] * extendedNums[j] * extendedNums[j + 1];
            for (int i = j - 1; i > 0; i--) {
                for (int last = i; last <= j; last++) {
                    dp[i][j] = max(dp[i][j], dp[i][last - 1] + extendedNums[i - 1] * extendedNums[last] * extendedNums[j + 1] + dp[last + 1][j]);
                }
            }
        }
        return dp[1][N];
    }
};

// @lc code=end

