/*
 * @lc app=leetcode id=452 lang=csharp
 *
 * [452] Minimum Number of Arrows to Burst Balloons
 */

// @lc code=start
public class Solution 
{
    public int FindMinArrowShots(int[][] points) 
    {
        points = points.OrderBy(x => x[0]).ThenBy(x => x[1]).Select(x => x).ToArray();
        int result = 1;
        int n = points.Length;
        int end = points[0][1];
        for (int i = 1; i < n; i++)
        {
            if (points[i][0] > end)
            {
                end = points[i][1];
                result++;
            }
            else if (points[i][1] < end)
            {
                end = points[i][1];
            }
        }
        return result;
    }
}
// @lc code=end
