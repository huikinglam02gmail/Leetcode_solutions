/*
 * @lc app=leetcode id=1653 lang=csharp
 *
 * [1653] Minimum Deletions to Make String Balanced
 */

// @lc code=start
public class Solution 
{
    public int MinimumDeletions(string s) 
    {
        int total = s.Count(x => x == 'a');
        int n = s.Length;
        int result = total;

        for (int i = 0; i < n; i++)
        {
            result = Math.Min(result, total);
            if (s[i] == 'a')
            {
                total--;
            }
            else
            {
                total++;
            }
        }
        return Math.Min(result, total);
    }
}
// @lc code=end

