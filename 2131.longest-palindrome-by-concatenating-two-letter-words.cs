/*
 * @lc app=leetcode id=2131 lang=csharp
 *
 * [2131] Longest Palindrome by Concatenating Two Letter Words
 */

// @lc code=start
public class Solution 
{
    public static string Reverse(string s)
    {
        char[] charArray = s.ToCharArray();
        Array.Reverse(charArray);
        return new string(charArray);
    }
    public int LongestPalindrome(string[] words) 
    {
        Dictionary<string, int> hashTable = new Dictionary<string, int>();
        foreach (string word in words)
        {
            if (!hashTable.ContainsKey(word))
            {
                hashTable[word] = 0;
            }
            hashTable[word] += 1;
        }
        int result = 0;
        HashSet<string> considered = new HashSet<string>();
        HashSet<string> sameOddSet = new HashSet<string>();
        foreach(KeyValuePair<string, int> kvp in hashTable)
        {
            string key = kvp.Key;
            string key1 = Reverse(key);
            int value = kvp.Value;
            if (!considered.Contains(key))
            {
                considered.Add(key);
                if (key[0] == key[1])
                {
                    result += 4*( value / 2);
                    if (value % 2 == 1)
                    {
                        sameOddSet.Add(key);
                    }
                }
                else if (hashTable.ContainsKey(key1))
                {
                    result += 4*Math.Min(value, hashTable[key1]);
                    if (!considered.Contains(key1))
                    {
                        considered.Add(key1);
                    }
                }
            }
        }
        if (sameOddSet.Count > 0)
        {
            result += 2;
        }
        return result;
    }
}
// @lc code=end

