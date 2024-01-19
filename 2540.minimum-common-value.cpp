/*
 * @lc app=leetcode id=2540 lang=cpp
 *
 * [2540] Minimum Common Value
 */

// @lc code=start
#include <vector>

class Solution {
public:
    /**
     * Basically two pointers:
     * i, j on nums1, nums2
     * If nums1[i] < nums2[j]: i++
     * ElseIf nums1[i] > nums2[j]: j++
     * Else return nums1[i]
     */
    int getCommon(std::vector<int>& nums1, std::vector<int>& nums2) {
        int i = 0, j = 0;
        while (i < nums1.size() && j < nums2.size()) {
            if (nums1[i] < nums2[j]) {
                i++;
            } else if (nums1[i] > nums2[j]) {
                j++;
            } else {
                return nums1[i];
            }
        }
        return -1;
    }
};

// @lc code=end

