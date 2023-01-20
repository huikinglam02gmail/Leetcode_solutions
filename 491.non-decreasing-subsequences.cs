/*
 * @lc app=leetcode id=491 lang=csharp
 *
 * [491] Non-decreasing Subsequences
 */

// @lc code=start
public class Solution 
{
    HashSet<string> seen;
    int[] data;
    List<IList<int>> result;
    public void dfs(int ind, int elements, int last, string current)
    {
        if (elements >= 2 && !seen.Contains(current))
        {
            seen.Add(current);
        }
        for (int i = ind; i < data.Length; i++)
        {
            if (string.IsNullOrEmpty(current))
            {
                dfs(i + 1, elements + 1, data[i], current + data[i].ToString());
            } 
            else if (data[i] >= last)
            {
                dfs(i + 1, elements + 1, data[i], current + "," + data[i].ToString());
            }
        }
    }

    public List<int> deserialize(string current)
    {
        string[] words = current.Split(",");
        return words.Select(x => Int32.Parse(x)).ToList();
    }

    public IList<IList<int>> FindSubsequences(int[] nums) 
    {
        seen = new HashSet<string>();
        data = nums;
        dfs(0, 0, -101, "");
        result = new List<IList<int>>();
        foreach (string word in seen)
        {
            result.Add(deserialize(word));
        }
        return result;
    }
}
// @lc code=end

