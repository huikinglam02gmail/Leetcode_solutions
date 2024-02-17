/*
 * @lc app=leetcode id=2824 lang=csharp
 *
 * [2824] Count Pairs Whose Sum is Less than Target
 */

// @lc code=start
using System;
using System.Linq;

public class Solution {
    public int CountPairs(int[] nums, int target) {
        Array.Sort(nums);
        int result = 0;
        for (int i = 0; i < nums.Length; i++) {
            int ind = Array.BinarySearch(nums, i + 1, nums.Length - i - 1, target - nums[i]);
            if (ind < 0) {
                ind = ~ind;
            }
            result += Math.Max(0, ind - i - 1);
        }
        return result;
    }
}

// @lc code=end

