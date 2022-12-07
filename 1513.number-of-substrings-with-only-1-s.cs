/*
 * @lc app=leetcode id=1513 lang=csharp
 *
 * [1513] Number of Substrings With Only 1s
 */

// @lc code=start
public class Solution 
{
    public int NumSub(string s) 
    {
        int consec = 0;
        long MOD = 1000000007;
        long result = 0;
        foreach (char c in s)
        {
            if (c == '1')
            {
                consec++;
            }
            else if (consec > 0)
            {
                result += consec*(consec + 1) / 2;
                result %= MOD;
                consec = 0;
            }
        }
        result += consec*(consec + 1) / 2;
        result %= MOD;
        return Convert.ToInt32(result);
    }
}
// @lc code=end

