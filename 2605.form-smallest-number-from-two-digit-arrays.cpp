/*
 * @lc app=leetcode id=2605 lang=cpp
 *
 * [2605] Form Smallest Number From Two Digit Arrays
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    /**
     * Brute force
     */
    int minNumber(std::vector<int>& nums1, std::vector<int>& nums2) {
        for (int i = 1; i < 100; i++) {
            if (i < 10 && std::find(nums1.begin(), nums1.end(), i) != nums1.end() && std::find(nums2.begin(), nums2.end(), i) != nums2.end())
                return i;
            else {
                int i1 = i / 10;
                int i2 = i % 10;
                if ((std::find(nums1.begin(), nums1.end(), i1) != nums1.end() && std::find(nums2.begin(), nums2.end(), i2) != nums2.end()) ||
                    (std::find(nums1.begin(), nums1.end(), i2) != nums1.end() && std::find(nums2.begin(), nums2.end(), i1) != nums2.end()))
                    return i;
            }
        }
        return -1;
    }
};

// @lc code=end

