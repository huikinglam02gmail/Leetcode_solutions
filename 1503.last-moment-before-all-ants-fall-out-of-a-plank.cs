/*
 * @lc app=leetcode id=1503 lang=csharp
 *
 * [1503] Last Moment Before All Ants Fall Out of a Plank
 */

// @lc code=start
public class Solution 
{
    public int GetLastMoment(int n, int[] left, int[] right) 
    {
        int result = 0;
        foreach (int num in left)
        {
            result = Math.Max(result, num);
        }
        foreach (int num in right)
        {
            result = Math.Max(result, n - num);
        }
        return result;
    }
}
// @lc code=end

