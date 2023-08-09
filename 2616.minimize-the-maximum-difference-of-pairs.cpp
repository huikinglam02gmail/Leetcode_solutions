/*
 * @lc app=leetcode id=2616 lang=cpp
 *
 * [2616] Minimize the Maximum Difference of Pairs
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
public:
    bool canForm(int p, int diff) {
        int pairs = 0;
        int i = 0;
        while (i < nums.size() - 1) {
            if (nums[i + 1] - nums[i] <= diff) {
                pairs++;
                i += 2;
            } else {
                i++;
            }
        }
        return pairs >= p;
    }

    int minimizeMax(std::vector<int>& nums, int p) {
        std::sort(nums.begin(), nums.end());
        this->nums = nums;
        int l = 0, r = nums[nums.size() - 1] - nums[0];
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (canForm(p, mid)) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }

private:
    std::vector<int> nums;
};

// @lc code=end

