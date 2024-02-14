/*
 * @lc app=leetcode id=2149 lang=csharp
 *
 * [2149] Rearrange Array Elements by Sign
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int[] RearrangeArray(int[] nums) {
        List<int>[] arrs = new List<int>[2];
        arrs[0] = new List<int>();
        arrs[1] = new List<int>();
        
        bool firstIsPositive = nums[0] > 0;
        
        foreach (int num in nums) {
            arrs[(num > 0) ^ firstIsPositive ? 1 : 0].Add(num);
        }
        
        List<int> result = new List<int>();
        
        for (int i = 0; i < nums.Length / 2; i++) {
            result.Add(arrs[1 - (firstIsPositive ? 1 : 0)][i]);
            result.Add(arrs[firstIsPositive ? 1 : 0][i]);
        }
        
        return result.ToArray();
    }
}

// @lc code=end

