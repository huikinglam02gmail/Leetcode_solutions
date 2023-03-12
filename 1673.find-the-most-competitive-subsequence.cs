/*
 * @lc app=leetcode id=1673 lang=csharp
 *
 * [1673] Find the Most Competitive Subsequence
 */

// @lc code=start
using System.Collections.Generic;
public class Solution 
{
    public int[] MostCompetitive(int[] nums, int k) 
    {
        List<int> stack = new List<int>();
        int n = nums.Length;
        for (int i = 0; i < n; i++)
        {
            while (stack.Count > 0 && nums[i] < stack[stack.Count - 1] && n - i + stack.Count - 1 >= k)
            {
                stack.RemoveAt(stack.Count - 1);
            }
            stack.Add(nums[i]);
        }    
        return stack.GetRange(0, k).ToArray();
    }
}
// @lc code=end

