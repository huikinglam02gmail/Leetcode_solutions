/*
 * @lc app=leetcode id=2187 lang=csharp
 *
 * [2187] Minimum Time to Complete Trips
 */

// @lc code=start
using System.Linq;
public class Solution 
{
    public long MinimumTime(int[] time, int totalTrips) 
    {
        long left = 0;
        long right = Convert.ToInt64(time.Max()) * Convert.ToInt64(totalTrips);
        while (left < right)
        {
            long mid = left + (right - left) / 2;
            long ans = time.Select(x => mid / Convert.ToInt64(x)).Sum();
            if (ans < totalTrips)
            {
                left = mid + 1;
            }
            else
            {
                right = mid;
            }
        }    
        return left;
    }
}
// @lc code=end
