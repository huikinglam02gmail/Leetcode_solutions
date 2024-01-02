/*
 * @lc app=leetcode id=2610 lang=cpp
 *
 * [2610] Convert an Array Into a 2D Array With Conditions
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<int>> findMatrix(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        std::vector<std::vector<int>> result;
        int prev = 0;
        int j = 0;

        for (int num : nums) {
            if (num != prev) {
                j = 0;
            }

            if (0 <= j && j < result.size()) {
                result[j].push_back(num);
            } else {
                result.push_back({num});
            }

            j++;
            prev = num;
        }

        return result;
    }
};

// @lc code=end

