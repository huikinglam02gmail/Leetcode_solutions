/*
 * @lc app=leetcode id=2971 lang=cpp
 *
 * [2971] Find Polygon With the Largest Perimeter
 */

// @lc code=start
#include <algorithm>
#include <vector>

class Solution {
public:
    long long largestPerimeter(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int n = nums.size();
        std::vector<long long> prefix(n + 1, 0);
        
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + (long long)nums[i];
        }
        
        for (int i = n - 1; i > 0; i--) {
            if ((long long)nums[i] < prefix[i]) {
                return (long long)nums[i] + prefix[i];
            }
        }
        
        return -1;
    }
};

// @lc code=end

