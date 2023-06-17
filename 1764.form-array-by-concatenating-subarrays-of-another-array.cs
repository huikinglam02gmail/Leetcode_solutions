/*
 * @lc app=leetcode id=1764 lang=csharp
 *
 * [1764] Form Array by Concatenating Subarrays of Another Array
 */

// @lc code=start
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public bool CanChoose(int[][] groups, int[] nums) 
    {
        List<string> groupString = groups.Select(group => "_" + string.Join("_", group)).ToList();
        string numsString = "_" + string.Join("_", nums);
        int i = 0, j = 0;

        while (i < numsString.Length && j < groupString.Count) {
            int ind = numsString.IndexOf(groupString[j], i);
            if (ind == -1) {
                return false;
            }
            else {
                i = ind + groupString[j].Length;
                j++;
            }
        }

        return j == groupString.Count;
    }
}

// @lc code=end

