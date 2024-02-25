/*
 * @lc app=leetcode id=2932 lang=csharp
 *
 * [2932] Maximum Strong Pair XOR I
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int MaximumStrongPairXor(int[] nums) {
        int result = 0;
        foreach (int num1 in nums) {
            foreach (int num2 in nums) {
                if (Math.Abs(num1 - num2) <= Math.Min(num1, num2)) {
                    result = Math.Max(result, num1 ^ num2);
                }
            }
        }
        return result;
    }
}

// @lc code=end

