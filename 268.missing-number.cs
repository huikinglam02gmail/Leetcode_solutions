/*
 * @lc app=leetcode id=268 lang=csharp
 *
 * [268] Missing Number
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    public int MissingNumber(int[] nums) {
        int defaultSum = nums.Length * (nums.Length + 1) / 2;
        foreach (int num in nums) {
            defaultSum -= num;
        }
        return defaultSum;
    }
}

// @lc code=end

