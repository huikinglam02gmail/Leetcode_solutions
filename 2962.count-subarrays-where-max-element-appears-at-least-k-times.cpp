/*
 * @lc app=leetcode id=2962 lang=cpp
 *
 * [2962] Count Subarrays Where Max Element Appears at Least K Times
 */

// @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        int maxNum = nums[0];
        for (int num : nums) {
            maxNum = max(maxNum, num);
        }
        
        vector<int> appear;
        long long result = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == maxNum) {
                appear.push_back(i);
            }
        }
        
        for (int i = 0; i < nums.size(); i++) {
            auto iter = upper_bound(appear.begin(), appear.end(), i);
            int index = iter - appear.begin();
            if (index >= k) {
                result += appear[index - k] + 1;
            }
        }
        
        return result;
    }
};

// @lc code=end

