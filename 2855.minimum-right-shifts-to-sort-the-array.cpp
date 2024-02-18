/*
 * @lc app=leetcode id=2855 lang=cpp
 *
 * [2855] Minimum Right Shifts to Sort the Array
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int minimumRightShifts(std::vector<int>& nums) {
        int maxSoFar = 0, minSoFar = 101, i = -1, j = -1, n = nums.size();
        for (int k = 0; k < n; k++) {
            if (nums[k] > maxSoFar) {
                maxSoFar = nums[k];
                i = k;
            }
            if (nums[k] < minSoFar) {
                minSoFar = nums[k];
                j = k;
            }
        }
        if ((i + 1) % n != j) return -1;
        int l = j;
        while (l != i && nums[(l + 1) % n] > nums[l]) {
            l++;
            l %= n;
        }
        if (l == i) return n - 1 - i;
        else return -1;
    }
};

// @lc code=end

