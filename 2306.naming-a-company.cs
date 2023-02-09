/*
 * @lc app=leetcode id=2306 lang=csharp
 *
 * [2306] Naming a Company
 */

// @lc code=start
public class Solution 
{
    public long DistinctNames(string[] ideas) 
    {
        HashSet<string>[] groups = new HashSet<string>[26];
        for (int i = 0; i < 26; i++)
        {
            groups[i] = new HashSet<string>();
        }    

        foreach (string idea in ideas)
        {
            groups[(int)idea[0] - (int)'a'].Add(idea.Substring(1));
        }

        long result = 0;
        for (int i = 0; i < 25; i++)
        {
            for (int j = i + 1; j < 26; j++)
            {
                HashSet<string> ans = new HashSet<string>(groups[i]);
                ans.IntersectWith(groups[j]);
                int l = ans.Count;
                result += 2 * (groups[i].Count - l) * (groups[j].Count - l);
            }
        }
        return result;
    }
}
// @lc code=end

