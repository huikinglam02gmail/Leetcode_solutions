/*
 * @lc app=leetcode id=1657 lang=csharp
 *
 * [1657] Determine if Two Strings Are Close
 */

// @lc code=start
public class Solution 
{
    public bool CloseStrings(string word1, string word2) 
    {
        int[] occur1 = new int[26];
        int[] occur2 = new int[26];
        Array.Fill(occur1, 0);
        Array.Fill(occur2, 0);

        if (word1.Length  != word2.Length)
        {
            return false;
        }

        for (int i = 0; i < word1.Length; i++)
        {
            occur1[(int) word1[i] - (int)'a']++;
            occur2[(int) word2[i] - (int)'a']++;
        }

        for (int i = 0; i < 26; i++)
        {
            if ((occur1[i] == 0 & occur2[i] != 0) || (occur1[i] > 0 & occur2[i] == 0))
            {
                return false;
            }
        }

        Array.Sort(occur1);
        Array.Sort(occur2);
        
        for (int i = 0; i < 26; i++)
        {
            if (occur1[i] != occur2[i])
            {
                return false;
            }
        }
        return true;
    }
}
// @lc code=end

