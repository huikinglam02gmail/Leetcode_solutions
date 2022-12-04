/*
 * @lc app=leetcode id=2256 lang=csharp
 *
 * [2256] Minimum Average Difference
 */

// @lc code=start
public class Solution 
{
    public int MinimumAverageDifference(int[] nums) 
    {
        int n = nums.Length;
        long[] prefix = new long[n + 1];
        prefix[0] = 0;
        for (int i = 0; i < n; i++)
        {
            prefix[i + 1] = prefix[i] + nums[i];
        }

        long minsofar = prefix[prefix.Length - 1] / n;
        int result = n - 1;

        for (int i = 0; i < n - 1; i++)
        {
            long current = Math.Abs(prefix[i+1] / (i+1) - (prefix[prefix.Length-1] - prefix[i+1]) / (n - i - 1));
            if (current < minsofar)
            {
                minsofar = current;
                result = i;
            }
            else if (current == minsofar && i < result)
            {
                result = i;
            }
        }
        return result;        
    }
}
// @lc code=end

