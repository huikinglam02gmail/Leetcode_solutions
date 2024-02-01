/*
 * @lc app=leetcode id=2966 lang=csharp
 *
 * [2966] Divide Array Into Arrays With Max Difference
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int[][] DivideArray(int[] nums, int k) {
        Array.Sort(nums);
        List<List<int>> result = new List<List<int>>();
        int n = nums.Length;

        for (int i = 0; i < n; i += 3) {
            if (i + 2 < n && nums[i + 2] - nums[i] > k) {
                return new int[0][]; // Return an empty list if the condition is not satisfied
            } else {
                result.Add(new List<int> { nums[i], nums[i + 1], nums[i + 2] });
            }
        }

        return result.Select(x => x.ToArray()).ToArray();
    }
}

// @lc code=end

