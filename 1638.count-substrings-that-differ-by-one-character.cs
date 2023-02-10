/*
 * @lc app=leetcode id=1638 lang=csharp
 *
 * [1638] Count Substrings That Differ by One Character
 */

// @lc code=start
public class Solution 
{
    public int CountSubstrings(string s, string t) 
    {
        int m = s.Length;
        int n = t.Length;   
        int[][] before = new int[m][];
        int[][] after = new int[m][];
        for (int i = 0; i < m; i++)
        {
            before[i] = new int[n];
            after[i] = new int[n];
            Array.Fill(before[i], 0);
            Array.Fill(after[i], 0);
        } 

        for (int i = 1; i < m; i++)
        {
            for (int j = 1; j < n; j++)
            {
                if (s[i - 1] == t[j - 1])
                {
                    before[i][j] = before[i - 1][j - 1] + 1;
                }
                else
                {
                    before[i][j] = 0;
                }
            }
        }
        for (int i = m - 2; i >= 0; i--)
        {
            for (int j = n - 2; j >= 0; j--)
            {
                if (s[i + 1] == t[j + 1])
                {
                    after[i][j] = after[i + 1][j + 1] + 1;
                }
                else
                {
                    after[i][j] = 0;
                }
            }
        }

        int result = 0;
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (s[i] != t[j])
                {
                    result += (before[i][j] + 1) * (after[i][j] + 1);
                }
            }
        }
        return result;
    }
}
// @lc code=end