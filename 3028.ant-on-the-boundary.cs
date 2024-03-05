/*
 * @lc app=leetcode id=3028 lang=csharp
 *
 * [3028] Ant on the Boundary
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int ReturnToBoundaryCount(int[] nums) {
        int result = 0;
        int x = 0;
        foreach (int num in nums) {
            x += num;
            if (x == 0) result++;
        }
        return result;
    }
}

// @lc code=end

