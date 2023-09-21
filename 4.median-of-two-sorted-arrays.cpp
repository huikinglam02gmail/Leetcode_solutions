/*
 * @lc app=leetcode id=4 lang=cpp
 *
 * [4] Median of Two Sorted Arrays
 */

// @lc code=start
#include <vector>

class Solution {
public:
    double findMedianSortedArrays(std::vector<int>& nums1, std::vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();

        if (m > n) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int l = 0;
        int r = m;

        while (l < r) {
            int x = l + (r - l) / 2;

            if (x < m && nums1[x] < nums2[(m + n) / 2 - x - 1]) {
                l = x + 1;
            } else {
                r = x;
            }
        }

        if ((m + n) % 2 == 1) {
            if (l < m) {
                return std::min(nums1[l], nums2[(m + n) / 2 - l]);
            } else {
                return nums2[(m + n) / 2 - l];
            }
        } else {
            double left1Lim = std::numeric_limits<double>::lowest();
            double left2Lim = std::numeric_limits<double>::lowest();
            double right1Lim = std::numeric_limits<double>::max();
            double right2Lim = std::numeric_limits<double>::max();

            if (l > 0) {
                left1Lim = static_cast<double>(nums1[l - 1]);
            }

            if ((m + n) / 2 - l > 0) {
                left2Lim = static_cast<double>(nums2[(m + n) / 2 - l - 1]);
            }

            if (l < m) {
                right1Lim = static_cast<double>(nums1[l]);
            }

            if ((m + n) / 2 - l < n) {
                right2Lim = static_cast<double>(nums2[(m + n) / 2 - l]);
            }

            return (std::max(left1Lim, left2Lim) + std::min(right1Lim, right2Lim)) / 2.0;
        }
    }
};

// @lc code=end

