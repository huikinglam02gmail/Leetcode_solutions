/*
 * @lc app=leetcode id=1540 lang=csharp
 *
 * [1540] Can Convert String in K Moves
 */

// @lc code=start
public class Solution 
{
    public bool CanConvertString(string s, string t, int k) 
    {
        if (s.Length != t.Length)
        {
            return false;
        }

        int[] counts = new int[26];
        Array.Fill(counts, 0);
        int n = s.Length;
        for (int i = 0; i < n; i++)
        {
            counts[((int) t[i] - (int) s[i] + 26) % 26]++;
        }
        for (int i = 1; i < 26; i++)
        {
            if (counts[i] > 0)
            {
                if (k / 26 + 1 < counts[i])
                {
                    return false;
                }
                else if (k / 26 + 1 == counts[i] && k % 26 < i)
                {
                    return false;
                }
            }
        }
        return true;
    }
}
// @lc code=end

