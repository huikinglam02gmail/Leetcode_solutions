/*
 * @lc app=leetcode id=3068 lang=csharp
 *
 * [3068] Find the Maximum Sum of Node Values
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    /*
    As the graph is a tree, we can always flip an even number of nodes (no need to care about the edges) to get a larger sum.
    That is, if count(num ^ k > num for num in nums) is even, we can return the maximum sum possible.
    For the case in which this count is odd, we have to reduce the maxSum by min(abs(num ^ k - num)), which points to the node in which num is closest to num ^ k. For example, in example 2, nums = [7, 3], k = 7, maxSum is 7 + 4 = 11, and count = 1. As count is odd, the maxSum has included a flip that violated the rule. We can choose the one which induced the least change, which is flip of 3 to 4.
    */
    public long MaximumValueSum(int[] nums, int k, int[][] edges)
    {
        int count = 0;
        long maxSum = 0;
        int sacrifice = int.MaxValue;

        foreach (var num in nums)
        {
            if ((num ^ k) > num) count++;
            sacrifice = Math.Min(sacrifice, Math.Abs((num ^ k) - num));
            maxSum += Math.Max(num, num ^ k);
        }

        if (count % 2 != 0) maxSum -= sacrifice;

        return maxSum;
    }
}

// @lc code=end

