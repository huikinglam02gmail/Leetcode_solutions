/*
 * @lc app=leetcode id=1593 lang=csharp
 *
 * [1593] Split a String Into the Max Number of Unique Substrings
 */

// @lc code=start
public class Solution 
{
    int result;
    string str;
    HashSet<string> seen;
    public void dfs(int i)
    {
        if (i == str.Length)
        {
            result = Math.Max(result, seen.Count);
        }
        else
        {
            for (int j = i; j < str.Length; j++)
            {
                if (!seen.Contains(str.Substring(i, j - i + 1)))
                {
                    seen.Add(str.Substring(i, j - i + 1));
                    dfs(j + 1);
                    seen.Remove(str.Substring(i, j - i + 1));
                }
            }
        }
    }
    public int MaxUniqueSplit(string s) 
    {
        result = 0;
        str = s;
        seen = new HashSet<string>();
        dfs(0);
        return result;
    }
}
// @lc code=end
