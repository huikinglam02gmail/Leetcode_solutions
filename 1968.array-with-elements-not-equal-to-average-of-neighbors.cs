/*
 * @lc app=leetcode id=1968 lang=csharp
 *
 * [1968] Array With Elements Not Equal to Average of Neighbors
 */

// @lc code=start
using System;
using System.Linq;

public class Solution {
    public int[] RearrangeArray(int[] nums) {
        int n = nums.Length;
        Array.Sort(nums);
        int[] result = new int[n];
        for (int i = 0; i < n; i += 2) {
            result[i] = nums[n - 1 - i / 2];
        }
        for (int i = 1; i < n; i += 2) {
            result[i] = nums[i / 2];
        }
        return result;
    }
}

// @lc code=end

