/*
 * @lc app=leetcode id=1451 lang=csharp
 *
 * [1451] Rearrange Words in a Sentence
 */

// @lc code=start
public class Solution 
{
    public string ArrangeWords(string text) 
    {
        string[] words = text.Split(' ');
        IEnumerable<string> query = words.OrderBy(word => word.Length);
        words = query.ToArray();
        words[0] = words[0][0].ToString().ToUpper() + words[0].Substring(1, words[0].Length - 1);
        for (int i = 1; i <  words.Length; i++)
        {
            words[i] = words[i][0].ToString().ToLower() + words[i].Substring(1, words[i].Length - 1);
        }
        return string.Join(" ", words);
    }
}
// @lc code=end

