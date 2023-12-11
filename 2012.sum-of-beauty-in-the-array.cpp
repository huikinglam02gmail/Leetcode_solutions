/*
 * @lc app=leetcode id=2012 lang=cpp
 *
 * [2012] Sum of Beauty in the Array
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <set>
#include <tuple>

using namespace std;

class Solution {
public:
    /*
    Use two sets left and right to denote left and right of each index
    Then iterate from i = 1 to n - 2
    */
    int sumOfBeauties(vector<int>& nums) {
        set<tuple<int, int>> left;
        set<tuple<int, int>> right;

        int n = nums.size();
        int result = 0;

        for (int i = 0; i < n; i++) {
            right.insert(make_tuple(nums[i], i));
        }

        for (int i = 0; i < n; i++) {
            right.erase(make_tuple(nums[i], i));

            if (0 < i && i < n - 1) {
                if (nums[i - 1] < nums[i] && nums[i] < nums[i + 1]) {
                    result++;
                }

                if (!left.empty() && get<0>(*left.rbegin()) < nums[i] && nums[i] < get<0>(*right.begin())) {
                    result++;
                }
            }

            left.insert(make_tuple(nums[i], i));
        }

        return result;
    }
};

// @lc code=end

