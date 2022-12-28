/*
 * @lc app=leetcode id=1573 lang=csharp
 *
 * [1573] Number of Ways to Split a String
 */

// @lc code=start
public class Solution 
{
    public int NumWays(string s) 
    {
        List<long> counts = new List<long>();
        int n = s.Length;
        long MOD = 1000000007;
        long result = 0;
        for (int i = 0; i < n; i++)
        {
            if (s[i] == '1')
            {
                counts.Add(i);
            }
        }
        if (counts.Count == 0)
        {
            for (int i = 1; i < n - 1; i++)
            {
                result += n - i - 1;
                result %= MOD;
            }
        }
        else if (counts.Count % 3 == 0)
        {
            int l = counts.Count / 3;
            result = ((counts[l] - counts[l-1]) * (counts[2*l] - counts[2*l - 1])) % MOD;
        }
        return Convert.ToInt32(result);
    }
}
// @lc code=end

