/*
 * @lc app=leetcode id=4 lang=csharp
 *
 * [4] Median of Two Sorted Arrays
 */

// @lc code=start
using System;

public class Solution {
    public double FindMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.Length;
        int n = nums2.Length;

        if (m > n) {
            return FindMedianSortedArrays(nums2, nums1);
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
                return Math.Min(nums1[l], nums2[(m + n) / 2 - l]);
            } else {
                return nums2[(m + n) / 2 - l];
            }
        } else {
            double left1Lim = double.NegativeInfinity;
            double left2Lim = double.NegativeInfinity;
            double right1Lim = double.PositiveInfinity;
            double right2Lim = double.PositiveInfinity;

            if (l > 0) {
                left1Lim = nums1[l - 1];
            }

            if ((m + n) / 2 - l > 0) {
                left2Lim = nums2[(m + n) / 2 - l - 1];
            }

            if (l < m) {
                right1Lim = nums1[l];
            }

            if ((m + n) / 2 - l < n) {
                right2Lim = nums2[(m + n) / 2 - l];
            }

            return (Math.Max(left1Lim, left2Lim) + Math.Min(right1Lim, right2Lim)) / 2;
        }
    }
}

// @lc code=end

