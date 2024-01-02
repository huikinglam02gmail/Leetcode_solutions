/*
 * @lc app=leetcode id=2610 lang=csharp
 *
 * [2610] Convert an Array Into a 2D Array With Conditions
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> FindMatrix(int[] nums) {
        Array.Sort(nums);
        List<IList<int>> result = new List<IList<int>>();
        int prev = 0;
        int j = 0;
        
        foreach (int num in nums) {
            if (num != prev) {
                j = 0;
            }

            if (0 <= j && j < result.Count) {
                result[j].Add(num);
            }
            else {
                result.Add(new List<int> { num });
            }

            j++;
            prev = num;
        }

        return result;
    }
}

// @lc code=end

