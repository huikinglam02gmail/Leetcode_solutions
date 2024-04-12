/*
 * @lc app=leetcode id=42 lang=csharp
 *
 * [42] Trapping Rain Water
 */

// @lc code=start
using System;

public class Solution {
    public int Trap(int[] height) {
        int result = 0;
        int n = height.Length;
        int[] leftMax = new int[n];
        int[] rightMax = new int[n];
        leftMax[0] = height[0];
        rightMax[n - 1] = height[n - 1];

        for (int i = 1; i < n; i++) {
            leftMax[i] = Math.Max(height[i], leftMax[i - 1]);
        }

        for (int i = n - 2; i >= 0; i--) {
            rightMax[i] = Math.Max(height[i], rightMax[i + 1]);
        }

        for (int i = 0; i < n; i++) {
            result += Math.Min(leftMax[i], rightMax[i]) - height[i];
        }

        return result;
    }
}

// @lc code=end

