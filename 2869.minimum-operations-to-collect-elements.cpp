/*
 * @lc app=leetcode id=2869 lang=cpp
 *
 * [2869] Minimum Operations to Collect Elements
 */

// @lc code=start
#include <vector>
#include <unordered_set>

class Solution {
public:
    int minOperations(std::vector<int>& nums, int k) {
        std::unordered_set<int> need;
        int n = nums.size();
        for (int i = 1; i <= k; i++) {
            need.insert(i);
        }
        while (!nums.empty() && !need.empty()) {
            int i = nums.back();
            nums.pop_back();
            if (need.count(i)) {
                need.erase(i);
            }
        }
        return n - nums.size();
    }
};

// @lc code=end

