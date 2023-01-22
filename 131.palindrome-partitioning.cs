/*
 * @lc app=leetcode id=131 lang=csharp
 *
 * [131] Palindrome Partitioning
 */

// @lc code=start
public class Solution 
{
    List<IList<string>> result;
    public bool isPalindrome(string s)
    {
        int l = 0;
        int r = s.Length - 1;
        while (l < r)
        {
            if (s[l] != s[r])
            {
                return false;
            }
            else
            {
                l++;
                r--;
            }
        }
        return true;
    }

    public void dfs(string s, List<string> path)
    {
        if (s.Length == 0)
        {
            result.Add(path.Select(x => x).ToList());
        }
        else
        {
            for (int i = 1; i < s.Length + 1; i++)
            {
                if (isPalindrome(s.Substring(0, i)))
                {
                    path.Add(s.Substring(0, i));
                    dfs(s.Substring(i), path);
                    path.RemoveAt(path.Count - 1);
                }
            }
        }
    }

    public IList<IList<string>> Partition(string s) 
    {
        result = new List<IList<string>>();
        dfs(s, new List<string>());
        return result;
    }
}
// @lc code=end

