/*
 * @lc app=leetcode id=1458 lang=csharp
 *
 * [1458] Max Dot Product of Two Subsequences
 */

// @lc code=start
using System;

public class Solution {
    public int MaxDotProduct(int[] nums1, int[] nums2) {
        int n1 = nums1.Length;
        int n2 = nums2.Length;
        int[,] dp = new int[n1 + 1, n2 + 1];

        int max1 = int.MinValue;
        int min1 = int.MaxValue;
        int max2 = int.MinValue;
        int min2 = int.MaxValue;

        foreach (int num in nums1) {
            max1 = Math.Max(max1, num);
            min1 = Math.Min(min1, num);
        }

        foreach (int num in nums2) {
            max2 = Math.Max(max2, num);
            min2 = Math.Min(min2, num);
        }

        if ((max1 < 0 && min2 > 0) || (max2 < 0 && min1 > 0)) {
            return Math.Max(max1 * min2, min1 * max2);
        }

        for (int i = n1 - 1; i >= 0; i--) {
            for (int j = n2 - 1; j >= 0; j--) {
                dp[i, j] = dp[i + 1, j + 1];
                if (nums1[i] * nums2[j] > 0) {
                    dp[i, j] += nums1[i] * nums2[j];
                }
                dp[i, j] = Math.Max(dp[i, j], dp[i + 1, j]);
                dp[i, j] = Math.Max(dp[i, j], dp[i, j + 1]);
            }
        }

        return dp[0, 0];
    }
}

// @lc code=end

