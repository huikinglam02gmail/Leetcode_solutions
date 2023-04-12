/*
 * @lc app=leetcode id=71 lang=csharp
 *
 * [71] Simplify Path
 */

// @lc code=start
using System.Collections.Generic;
public class Solution 
{
    public string SimplifyPath(string path) 
    {
        string[] pathSplit = path.Split('/');
        List<string> result = new List<string>();
        foreach (string c in pathSplit)
        {
            if (c.Equals(".."))
            {
                if (result.Count > 0)
                {
                    result.RemoveAt(result.Count - 1);
                }
            }
            else if (!string.IsNullOrEmpty(c) && !c.Equals("."))
            {
                result.Add(c);
            }
        }
        return "/" + string.Join('/', result);
    }
}
// @lc code=end

