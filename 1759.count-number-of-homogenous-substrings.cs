/*
 * @lc app=leetcode id=1759 lang=csharp
 *
 * [1759] Count Number of Homogenous Substrings
 */

// @lc code=start
public class Solution
{
    /*
    Can only form substrings with all same characters within chunks.
    For a chunk of length l, the number of substrings = 1 + 2 + ... + l = l * (l + 1) // 2
    */
    public int CountHomogenous(string s)
    {
        const long MOD = 1000000007;
        int n = s.Length;
        int l = 0;
        long result = 0;

        while (l < n)
        {
            int r = l + 1;
            while (r < n && s[l] == s[r])
            {
                r++;
            }

            result += (Convert.ToInt64(r - l)) * (Convert.ToInt64(r - l + 1)) / 2;
            result %= MOD;
            l = r;
        }

        return Convert.ToInt32(result);
    }
}

// @lc code=end

