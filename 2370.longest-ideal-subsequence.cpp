/*
 * @lc app=leetcode id=2370 lang=cpp
 *
 * [2370] Longest Ideal Subsequence
 */

// @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int longestIdealString(string s, int k) {
        vector<int> dp(26, 0);
        for (char c : s) {
            int index = c - 'a';
            int curr = 0;
            for (int i = index - k; i <= index + k; i++) {
                if (0 <= i && i < 26) {
                    curr = max(curr, dp[i] + 1);
                }
            }
            dp[index] = curr;
        }
        int maxCount = 0;
        for (int count : dp) {
            maxCount = max(maxCount, count);
        }
        return maxCount;
    }
};

// @lc code=end

