/*
 * @lc app=leetcode id=926 lang=csharp
 *
 * [926] Flip String to Monotone Increasing
 */

// @lc code=start
public class Solution 
{
    public int MinFlipsMonoIncr(string s) 
    {
        int counter = 0;
        int flips = 0;
        foreach (char c in s)
        {
            if (c == '1')
            {
                counter++;
            }
            else
            {
                flips = Math.Min(flips + 1, counter);
            }
        }    
        return flips;
    }
}
// @lc code=end

