/*
 * @lc app=leetcode id=1526 lang=csharp
 *
 * [1526] Minimum Number of Increments on Subarrays to Form a Target Array
 */

// @lc code=start
public class Solution 
{
    public int MinNumberOperations(int[] target) 
    {
        int prev = 0;
        int n = target.Length;
        int result = 0;
        for (int i = 0; i < n; i++)
        {
            result += Math.Max(target[i] - prev, 0);
            prev = target[i];
        }
        return result;
    }
}
// @lc code=end

