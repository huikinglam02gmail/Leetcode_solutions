/*
 * @lc app=leetcode id=977 lang=csharp
 *
 * [977] Squares of a Sorted Array
 */

// @lc code=start
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] SortedSquares(int[] nums) {
        Array.Sort(nums, (x, y) => x * x - y * y);
        return nums.Select(num => num * num).ToArray();
    }
}

// @lc code=end

