/*
 * @lc app=leetcode id=1529 lang=csharp
 *
 * [1529] Minimum Suffix Flips
 */

// @lc code=start
public class Solution 
{
    public int MinFlips(string target) 
    {
        char prev = '0';
        int result = 0;
        foreach (char c in target)
        {
            if (c != prev)
            {
                result++;
                prev = c;
            }
        }
        return result;
    }   
}
// @lc code=end

