/*
 * @lc app=leetcode id=438 lang=csharp
 *
 * [438] Find All Anagrams in a String
 */

// @lc code=start
public class Solution 
{
    public IList<int> FindAnagrams(string s, string p) 
    {
        List<int> result = new List<int>();
        if (p.Length <= s.Length)
        {
            int[] hashP = new int[26];
            int[] hashS = new int[26];
            Array.Fill(hashP, 0);
            Array.Fill(hashS, 0);

            foreach(char c in p)
            {
                hashP[(int)c - (int)'a']++;
            }
            for (int i = 0; i < s.Length; i++)
            {
                hashS[(int)s[i] - (int)'a']++;
                if (i >= p.Length)
                {
                    hashS[(int)s[i - p.Length] - (int)'a']--;
                }

                if (hashS.SequenceEqual(hashP))
                {
                    result.Add(i + 1 - p.Length);
                }
            }
        }   
        return result;
    }
}
// @lc code=end

