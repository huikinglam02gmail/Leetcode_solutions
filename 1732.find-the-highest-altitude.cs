/*
 * @lc app=leetcode id=1732 lang=csharp
 *
 * [1732] Find the Highest Altitude
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int LargestAltitude(int[] gain) {
        int currentMax = 0;
        int currentHeight = 0;
        foreach (int i in gain) {
            currentHeight += i;
            currentMax = Math.Max(currentMax, currentHeight);
        }
        return currentMax;
    }
}

// @lc code=end

