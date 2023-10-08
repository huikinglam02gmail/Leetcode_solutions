/*
 * @lc app=leetcode id=1458 lang=cpp
 *
 * [1458] Max Dot Product of Two Subsequences
 */

// @lc code=start
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxDotProduct(vector<int>& nums1, vector<int>& nums2) {
        int n1 = nums1.size();
        int n2 = nums2.size();
        vector<vector<int>> dp(n1 + 1, vector<int>(n2 + 1, 0));

        int max1 = INT_MIN;
        int min1 = INT_MAX;
        int max2 = INT_MIN;
        int min2 = INT_MAX;

        for (int num : nums1) {
            max1 = max(max1, num);
            min1 = min(min1, num);
        }

        for (int num : nums2) {
            max2 = max(max2, num);
            min2 = min(min2, num);
        }

        if ((max1 < 0 && min2 > 0) || (max2 < 0 && min1 > 0)) {
            return max(max1 * min2, min1 * max2);
        }

        for (int i = n1 - 1; i >= 0; i--) {
            for (int j = n2 - 1; j >= 0; j--) {
                dp[i][j] = dp[i + 1][j + 1];
                if (nums1[i] * nums2[j] > 0) {
                    dp[i][j] += nums1[i] * nums2[j];
                }
                dp[i][j] = max(dp[i][j], dp[i + 1][j]);
                dp[i][j] = max(dp[i][j], dp[i][j + 1]);
            }
        }

        return dp[0][0];
    }
};

// @lc code=end

