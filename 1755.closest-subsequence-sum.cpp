/*
 * @lc app=leetcode id=1755 lang=cpp
 *
 * [1755] Closest Subsequence Sum
 */

// @lc code=start
#include<vector>
#include<algorithm>
using std::abs;
using std::lower_bound;
using std::make_move_iterator;
using std::min;
using std::sort;
using std::vector;
class Solution {
private:
    vector<int> dpSumBitMaskSorted(vector<int>& nums) {
    int l = nums.size();
    vector<int> result { 0 };
    for (int i = 0; i < l; i++) {
        for (int j = (1 << i); j < (1 << (i + 1)); j++) {
            result.push_back(nums[i] + result[j - (1 << i)]);
        }
    }
    sort(result.begin(), result.end());
    return result;
}

public:
    int minAbsDifference(vector<int>& nums, int goal) {
        int n = nums.size();
        if (n == 1) {
            return min(abs(nums[0] - goal), abs(goal));
        } else {
            vector<int> right(make_move_iterator(nums.begin() + nums.size()/2), make_move_iterator(nums.end()));
            nums.erase(nums.begin() + nums.size()/2, nums.end());

            vector<int> leftSumSorted = dpSumBitMaskSorted(nums);
            vector<int> rightSumSorted = dpSumBitMaskSorted(right);
            int nr = rightSumSorted.size();
            int result = INT_MAX;
            for (int i : leftSumSorted) {
                int ind = lower_bound(rightSumSorted.begin(), rightSumSorted.end(), goal - i) - rightSumSorted.begin();
                if (ind - 1 >= 0 && ind - 1 < nr) {
                    result = min(result, abs(rightSumSorted[ind - 1] + i - goal));
                }
                if (ind >= 0 && ind < nr) {
                    result = min(result, abs(rightSumSorted[ind] + i - goal));
                }
                if (ind + 1 >= 0 && ind + 1 < nr) {
                    result = min(result, abs(rightSumSorted[ind + 1] + i - goal));
                }
            }
            return result;
        }        
    }
};
// @lc code=end

