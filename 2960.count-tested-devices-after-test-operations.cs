/*
 * @lc app=leetcode id=2960 lang=csharp
 *
 * [2960] Count Tested Devices After Test Operations
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    public int CountTestedDevices(int[] batteryPercentages) {
        int result = 0;
        int deducted = 0;
        int i = 0;
        while (i < batteryPercentages.Length) {
            if (batteryPercentages[i] - deducted > 0) {
                result++;
                deducted++;
            }
            i++;
        }
        return result;
    }
}

// @lc code=end

