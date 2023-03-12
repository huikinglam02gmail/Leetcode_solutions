/*
 * @lc app=leetcode id=1674 lang=csharp
 *
 * [1674] Minimum Moves to Make Array Complementary
 */

// @lc code=start
using System;
public class Solution 
{
    public int MinMoves(int[] nums, int limit) 
    {
        int[] prefix = new int[2*(limit + 1)];
        int n = nums.Length;
        Array.Fill(prefix, 0);    

        for (int i = 0; i < n / 2; i++)
        {
            int a = Math.Min(nums[i], nums[n - 1 - i]);
            int b = Math.Max(nums[i], nums[n - 1 - i]);
            prefix[0] += 2;
            prefix[a + 1]--;
            prefix[a + b]--;
            prefix[a + b + 1]++;
            prefix[b + limit + 1]++;            
        }

        int result = n;
        int prefixSum = 0;
        for (int i = 0; i < 2*(limit + 1); i++)
        {
            prefixSum += prefix[i];
            result = Math.Min(result, prefixSum);
        }
        return result;
    }
}
// @lc code=end

