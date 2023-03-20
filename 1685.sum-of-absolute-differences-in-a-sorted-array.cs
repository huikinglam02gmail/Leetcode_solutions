/*
 * @lc app=leetcode id=1685 lang=csharp
 *
 * [1685] Sum of Absolute Differences in a Sorted Array
 */

// @lc code=start
using System.Collections.Generic;
public class Solution 
{
    public int[] GetSumAbsoluteDifferences(int[] nums) 
    {
        List<int> prefix = new List<int>() {0};   
        foreach (int num in nums)
        {
            prefix.Add(prefix[prefix.Count - 1] + num);
        }

        List<int> result = new List<int>();
        int n = nums.Length;
        for (int i = 0; i < n; i++)
        {
            result.Add((2 * i - n) * nums[i] - 2 * prefix[i] + prefix[prefix.Count - 1]);
        }
        return result.ToArray();
    }
}
// @lc code=end

