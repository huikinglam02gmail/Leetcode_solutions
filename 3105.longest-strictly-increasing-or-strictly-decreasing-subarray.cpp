/*
 * @lc app=leetcode id=3105 lang=cpp
 *
 * [3105] Longest Strictly Increasing or Strictly Decreasing Subarray
 */

// @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    /*
    Keep track of last num, result so far, current longest strictly increasing and strictly decreasing subarray ending at num
    */
    int longestMonotonicSubarray(vector<int>& nums) {
        int currentIncr = 1, currentDecr = 1, result = 1, n = nums.size();
        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[i - 1]) {
                currentIncr++;
            } else {
                currentIncr = 1;
            }
            if (nums[i] < nums[i - 1]) {
                currentDecr++;
            } else {
                currentDecr = 1;
            }
            result = max(result, currentIncr);
            result = max(result, currentDecr);
        }
        return result;
    }
};

// @lc code=end

