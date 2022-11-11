/*
 * @lc app=leetcode id=1446 lang=csharp
 *
 * [1446] Consecutive Characters
 */

// @lc code=start
public class Solution 
{
    public int MaxPower(string s) 
    {
        char last = 'A';
        int power = 0;
        int result = 0;
        foreach (char c in s)
        {
            if (c == last)
            {
                power += 1;
            }
            else
            {
                power = 1;
            }
            result = Math.Max(result, power);
            last = c;
        }
        return result;
    }
}
// @lc code=end

