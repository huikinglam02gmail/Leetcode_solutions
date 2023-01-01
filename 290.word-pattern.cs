/*
 * @lc app=leetcode id=290 lang=csharp
 *
 * [290] Word Pattern
 */

// @lc code=start
public class Solution 
{
    public bool WordPattern(string pattern, string s) 
    {
        string[] sSplit = s.Split(' ');
        Dictionary<char,string> hashTable = new Dictionary<char,string>();
        HashSet<string> seen;
        if (pattern.Length != sSplit.Length)
        {
            return false;
        }
        seen = new HashSet<string>();
        for (int i = 0; i < pattern.Length; i++)
        {
            if (hashTable.ContainsKey(pattern[i]) && sSplit[i] != hashTable[pattern[i]])
            {
                return false;
            }
            else if (!hashTable.ContainsKey(pattern[i]) && seen.Contains(sSplit[i]))
            {
                return false;
            }
            else
            {
                hashTable[pattern[i]] = sSplit[i];
                seen.Add(sSplit[i]);
            }
        }
        return true;
    }
}
// @lc code=end

