/*
 * @lc app=leetcode id=3069 lang=cpp
 *
 * [3069] Distribute Elements Into Two Arrays I
 */

// @lc code=start
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> resultArray(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> arrs(2);
        for (int i = 0; i < n; i++) {
            if (i < 2) arrs[i].push_back(nums[i]);
            else if (arrs[0].back() > arrs[1].back()) arrs[0].push_back(nums[i]);
            else arrs[1].push_back(nums[i]);
        }
        vector<int> result;
        result.insert(result.end(), arrs[0].begin(), arrs[0].end());
        result.insert(result.end(), arrs[1].begin(), arrs[1].end());
        return result;
    }
};

// @lc code=end

