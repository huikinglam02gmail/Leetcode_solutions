/*
 * @lc app=leetcode id=2980 lang=csharp
 *
 * [2980] Check if Bitwise OR Has Trailing Zeros
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    public bool HasTrailingZeros(int[] nums) {
        int count = 0;
        foreach (int num in nums) {
            if (num % 2 == 0) {
                count++;
            }
        }
        return count > 1;
    }
}

// @lc code=end

