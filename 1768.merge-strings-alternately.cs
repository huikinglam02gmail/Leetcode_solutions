/*
 * @lc app=leetcode id=1768 lang=csharp
 *
 * [1768] Merge Strings Alternately
 */

// @lc code=start
using System.Text;
public class Solution 
{
    public string MergeAlternately(string word1, string word2) 
    {
        int i = 0;
        int j = 0;
        StringBuilder result = new StringBuilder();
        while (i < word1.Length && j < word2.Length) {
            result.Append(word1[i]);
            result.Append(word2[j]);
            i += 1;
            j += 1;
        }
        while (i < word1.Length) {
            result.Append(word1[i]);
            i += 1;
        }
        while (j < word2.Length) {
            result.Append(word2[j]);
            j += 1;
        }
        return result.ToString();
    }
}
// @lc code=end

