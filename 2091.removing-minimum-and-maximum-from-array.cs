/*
 * @lc app=leetcode id=2091 lang=csharp
 *
 * [2091] Removing Minimum and Maximum From Array
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    /*
    Identify indices of max and min
    There are 3 possibilities:
    1. delete both from left
    2. delete min(minInd, maxInd) from left and max(minInd, maxInd) from right
    3. delete both from right
    */
    public int MinimumDeletions(int[] nums) {
        int n = nums.Length;
        int[] result = new int[3];
        int maxInd = -1, maxNum = int.MinValue, minInd = -1, minNum = int.MaxValue;
        for (int i = 0; i < n; i++) {
            if (nums[i] > maxNum) {
                maxNum = nums[i];
                maxInd = i;
            }
            if (nums[i] < minNum) {
                minNum = nums[i];
                minInd = i;
            }
        }
        result[0] = Math.Max(maxInd, minInd) + 1;
        result[2] = n - Math.Min(maxInd, minInd);
        result[1] = Math.Min(minInd, maxInd) + 1 + n - Math.Max(minInd, maxInd);
        return Math.Min(result[0], Math.Min(result[1], result[2]));
    }
}

// @lc code=end

