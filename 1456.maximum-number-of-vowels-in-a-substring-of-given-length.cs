/*
 * @lc app=leetcode id=1456 lang=csharp
 *
 * [1456] Maximum Number of Vowels in a Substring of Given Length
 */

// @lc code=start
public class Solution 
{
    public int MaxVowels(string s, int k) 
    {
        int current = 0;
        int result = 0;
        int n = s.Length;
        for (int i = 0; i < k; i++)
        {
            if ("aeiou".Contains(s[i]))
            {
                current++;
            }
        }
        result = current;
        for (int i = k; i < n; i++)
        {
            if ("aeiou".Contains(s[i]))
            {
                current++;
            }
            if ("aeiou".Contains(s[i-k]))
            {
                current--;
            }
            result = Math.Max(result, current);
        }
        return result;   
    }
}
// @lc code=end

