/*
 * @lc app=leetcode id=1877 lang=csharp
 *
 * [1877] Minimize Maximum Pair Sum in Array
 */

// @lc code=start
using System;
using System.Linq;

public class Solution {
    public int MinPairSum(int[] nums) {
        Array.Sort(nums);
        int i = 0, j = nums.Length - 1;
        int result = 0;
        while (i < j) {
            result = Math.Max(result, nums[i] + nums[j]);
            i++;
            j--;
        }
        return result;
    }
}

// @lc code=end

