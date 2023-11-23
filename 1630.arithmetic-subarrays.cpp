/*
 * @lc app=leetcode id=1630 lang=cpp
 *
 * [1630] Arithmetic Subarrays
 */

// @lc code=start
#include <vector>

class Solution {
public:
    /*
     * No shortcut, just brute force    
     */
    bool canMakeArithmeticProgression(std::vector<int>& arr) {
        std::sort(arr.begin(), arr.end());
        int diff = arr[1] - arr[0];
        int n = arr.size();
        for (int i = 1; i < n - 1; i++) {
            if (arr[i] + diff != arr[i + 1]) {
                return false;
            }
        }
        return true;
    }

    std::vector<bool> checkArithmeticSubarrays(std::vector<int>& nums, std::vector<int>& l, std::vector<int>& r) {
        std::vector<bool> result;
        for (size_t i = 0; i < l.size(); i++) {
            std::vector<int> subarray(nums.begin() + l[i], nums.begin() + r[i] + 1);
            result.push_back(canMakeArithmeticProgression(subarray));
        }
        return result;
    }
};

// @lc code=end

