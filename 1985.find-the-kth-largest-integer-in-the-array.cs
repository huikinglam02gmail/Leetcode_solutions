/*
 * @lc app=leetcode id=1985 lang=csharp
 *
 * [1985] Find the Kth Largest Integer in the Array
 */

// @lc code=start
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public string KthLargestNumber(string[] nums, int k) {
        List<Tuple<string, int>> arr = new List<Tuple<string, int>>();
        int n = nums.Select(x=>x.Length).Max();

        foreach (var num in nums) {
            arr.Add(new Tuple<string, int>(num.PadLeft(n, '0'), arr.Count));
        }

        arr.Sort((a, b) => string.Compare(b.Item1, a.Item1, StringComparison.Ordinal));

        return nums[arr[k - 1].Item2];
    }
}

// @lc code=end

