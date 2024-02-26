/*
 * @lc app=leetcode id=3024 lang=csharp
 *
 * [3024] Type of Triangle
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public string TriangleType(int[] nums) {
        Array.Sort(nums);
        if (nums[0] + nums[1] <= nums[2]) {
            return "none";
        }
        int distinctCount = new HashSet<int>(nums).Count;
        switch (distinctCount) {
            case 1:
                return "equilateral";
            case 2:
                return "isosceles";
            case 3:
                return "scalene";
            default:
                throw new ArgumentException("Invalid input");
        }
    }
}

// @lc code=end

