/*
 * @lc app=leetcode id=2033 lang=csharp
 *
 * [2033] Minimum Operations to Make a Uni-Value Grid
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int MinOperations(int[][] grid, int x) {
        int m = grid.Length;
        int n = grid[0].Length;

        List<int> nums = new List<int>();

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                nums.Add(grid[i][j]);
            }
        }

        nums.Sort();

        if (x > 1) {
            for (int i = 1; i < m * n; i++) {
                if ((nums[i] - nums[0]) % x != 0) {
                    return -1;
                }
            }
        }

        int result = 0;
        int targetIndex = m * n / 2;

        foreach (int num in nums) {
            result += (int)Math.Abs(num - nums[targetIndex]) / x;
        }

        return result;
    }
}

// @lc code=end

