/*
 * @lc app=leetcode id=1846 lang=csharp
 *
 * [1846] Maximum Element After Decreasing and Rearranging
 */

// @lc code=start
using System;
using System.Linq;

public class Solution {
    public int MaximumElementAfterDecrementingAndRearranging(int[] arr) {
        Array.Sort(arr);
        int pre = 0;
        foreach (int a in arr) {
            pre = Math.Min(pre + 1, a);
        }
        return pre;
    }
}

// @lc code=end

