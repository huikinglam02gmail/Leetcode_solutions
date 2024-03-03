/*
 * @lc app=leetcode id=3069 lang=csharp
 *
 * [3069] Distribute Elements Into Two Arrays I
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int[] ResultArray(int[] nums) {
        int n = nums.Length;
        List<int>[] arrs = new List<int>[2];
        arrs[0] = new List<int>();
        arrs[1] = new List<int>();
        for (int i = 0; i < n; i++) {
            if (i < 2) arrs[i].Add(nums[i]);
            else if (arrs[0][arrs[0].Count - 1] > arrs[1][arrs[1].Count - 1]) arrs[0].Add(nums[i]);
            else arrs[1].Add(nums[i]);
        }
        List<int> result = new List<int>();
        result.AddRange(arrs[0]);
        result.AddRange(arrs[1]);
        return result.ToArray();
    }
}

// @lc code=end

