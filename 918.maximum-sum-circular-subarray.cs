/*
 * @lc app=leetcode id=918 lang=csharp
 *
 * [918] Maximum Sum Circular Subarray
 */

// @lc code=start
public class Solution 
{
    public int MaxSubarraySumCircular(int[] nums) 
    {
        double maxSum = 0;
        double minSum = 0;
        double maxSoFar = double.NegativeInfinity;
        double minSoFar = double.PositiveInfinity;
        double total = 0;

        foreach (int num in nums)
        {
            maxSum = Math.Max(maxSum + num, num);
            minSum = Math.Min(minSum + num, num);
            maxSoFar = Math.Max(maxSoFar, maxSum);
            minSoFar = Math.Min(minSoFar, minSum);
            total += num;
        }
        if (maxSoFar > 0)
        {
            return Convert.ToInt32(Math.Max(maxSoFar, total - minSoFar));
        }
        else
        {
            return Convert.ToInt32(maxSoFar);
        }
    }
}
// @lc code=end

