/*
 * @lc app=leetcode id=953 lang=csharp
 *
 * [953] Verifying an Alien Dictionary
 */

// @lc code=start
public class Solution 
{
    public string alienToHuman(string word, Dictionary<char, char> dict)
    {
        StringBuilder sb = new StringBuilder();
        foreach (char c in word)
        {
            sb.Append(dict[c]);
        }
        return sb.ToString();
    }
    public bool IsAlienSorted(string[] words, string order) 
    {
        Dictionary<char, char> alien = new Dictionary<char, char>();
        for (int i = 0; i < 26; i++)
        {
            alien.Add(order[i], Convert.ToChar(i + (int)'a'));
        }    

        string last = alienToHuman(words[0], alien);
        for (int i = 1; i < words.Length; i++)
        {
            string newWord = alienToHuman(words[i], alien);
            if (string.Compare(newWord, last) == -1)
            {
                return false;
            }
            else
            {
                last = newWord;
            }
        }
        return true;
    }
}
// @lc code=end

