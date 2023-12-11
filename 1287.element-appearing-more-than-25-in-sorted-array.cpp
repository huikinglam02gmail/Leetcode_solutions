/*
 * @lc app=leetcode id=1287 lang=cpp
 *
 * [1287] Element Appearing More Than 25% In Sorted Array
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int findSpecialInteger(std::vector<int>& arr) {
        int n = arr.size();
        if (n / 4 == 0) {
            return arr[0];
        }
        for (int i = 0; i < n; i += n / 4) {
            int count = std::count(arr.begin(), arr.end(), arr[i]);
            if (count > n / 4) {
                return arr[i];
            }
        }
        return -1;
    }
};

// @lc code=end

