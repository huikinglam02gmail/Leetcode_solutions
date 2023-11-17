/*
 * @lc app=leetcode id=1985 lang=cpp
 *
 * [1985] Find the Kth Largest Integer in the Array
 */

// @lc code=start
#include <vector>
#include <algorithm>
#include <string>

using std::string;

using std::max;

class Solution {
public:
    std::string kthLargestNumber(std::vector<std::string>& nums, int k) {
        std::vector<std::pair<std::string, int>> arr;
        int n = 0;

        for (int i = 0; i < nums.size(); ++i) {
            n = std::max(n, static_cast<int>(nums[i].length()));
        }

        for (int i = 0; i < nums.size(); ++i) {
            arr.push_back(std::make_pair(std::string(n - nums[i].length(), '0') + nums[i], i));
        }

        std::sort(arr.begin(), arr.end(), [](const auto& a, const auto& b) {
            return b.first < a.first;
        });

        return nums[arr[k - 1].second];
    }
};

// @lc code=end

