/*
 * @lc app=leetcode id=151 lang=csharp
 *
 * [151] Reverse Words in a String
 */

// @lc code=start
public class Solution 
{
    public string ReverseWords(string s) 
    {
        string[] sSplit = s.Split(' ');
        List<string> result = new List<string>();
        for (int i = sSplit.Length - 1; i >= 0; i--)
        {
            if (sSplit[i] != "")
            {
                result.Add(sSplit[i]);
            }
        }
        return String.Join(" ", result);   
    }
}
// @lc code=end

