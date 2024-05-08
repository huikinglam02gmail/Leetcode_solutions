/*
 * @lc app=leetcode id=506 lang=csharp
 *
 * [506] Relative Ranks
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public string[] FindRelativeRanks(int[] score) {
        var data = new List<int[]>();
        for (int i = 0; i < score.Length; i++) {
            data.Add(new int[] { score[i], i });
        }
        data.Sort((x, y) => y[0].CompareTo(x[0]));
        int n = score.Length;
        var result = new string[n];
        for (int i = 0; i < n; i++) {
            if (i == 0) result[data[i][1]] = "Gold Medal";
            else if (i == 1) result[data[i][1]] = "Silver Medal";
            else if (i == 2) result[data[i][1]] = "Bronze Medal";
            else result[data[i][1]] = (i + 1).ToString();
        }
        return result;
    }
}

// @lc code=end

