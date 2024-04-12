/*
 * @lc app=leetcode id=42 lang=cpp
 *
 * [42] Trapping Rain Water
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int trap(std::vector<int>& height) {
        int result = 0;
        int n = height.size();
        std::vector<int> leftMax(n, 0);
        std::vector<int> rightMax(n, 0);
        leftMax[0] = height[0];
        rightMax[n - 1] = height[n - 1];

        for (int i = 1; i < n; i++) {
            leftMax[i] = std::max(height[i], leftMax[i - 1]);
        }

        for (int i = n - 2; i >= 0; i--) {
            rightMax[i] = std::max(height[i], rightMax[i + 1]);
        }

        for (int i = 0; i < n; i++) {
            result += std::min(leftMax[i], rightMax[i]) - height[i];
        }

        return result;
    }
};

// @lc code=end

