/*
 * @lc app=leetcode id=1879 lang=csharp
 *
 * [1879] Minimum XOR Sum of Two Arrays
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    private int[] nums1;
    private int[] nums2;
    private Dictionary<(int, int), int> memo = new Dictionary<(int, int), int>();

    public int MinimumXORSum(int[] nums1, int[] nums2)
    {
        this.nums1 = nums1;
        this.nums2 = nums2;
        return DP(0, 0);
    }

    private int DP(int i, int mask)
    {
        if (i == nums1.Length)
            return 0;

        if (memo.ContainsKey((i, mask)))
            return memo[(i, mask)];

        int result = int.MaxValue;
        for (int j = 0; j < nums1.Length; j++)
        {
            if ((mask & (1 << j)) == 0)
            {
                result = Math.Min(result, (nums1[i] ^ nums2[j]) + DP(i + 1, mask ^ (1 << j)));
            }
        }

        memo[(i, mask)] = result;
        return result;
    }
}

// @lc code=end

