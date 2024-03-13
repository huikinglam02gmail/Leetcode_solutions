/*
 * @lc app=leetcode id=3074 lang=cpp
 *
 * [3074] Apple Redistribution into Boxes
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int minimumBoxes(std::vector<int>& apple, std::vector<int>& capacity) {
        std::sort(capacity.begin(), capacity.end(), std::greater<int>());
        std::vector<int> prefix = {0};
        for (int c : capacity) {
            prefix.push_back(prefix.back() + c);
        }
        int appleSum = 0;
        for (int a : apple) {
            appleSum += a;
        }
        return std::lower_bound(prefix.begin(), prefix.end(), appleSum) - prefix.begin();
    }
};

// @lc code=end

