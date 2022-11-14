/*
 * @lc app=leetcode id=1455 lang=csharp
 *
 * [1455] Check If a Word Occurs As a Prefix of Any Word in a Sentence
 */

// @lc code=start
public class Solution 
{
    public int IsPrefixOfWord(string sentence, string searchWord) 
    {
        string[] words = sentence.Split(" ");
        for (int i = 0; i < words.Length; i++)
        {
            if (words[i].StartsWith(searchWord))
            {
                return i + 1;
            }
        }
        return -1;
    }
}
// @lc code=end

