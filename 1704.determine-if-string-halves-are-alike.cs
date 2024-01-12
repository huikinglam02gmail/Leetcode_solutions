/*
 * @lc app=leetcode id=1704 lang=csharp
 *
 * [1704] Determine if String Halves Are Alike
 */

// @lc code=start
public class Solution 
{
    public bool HalvesAreAlike(string s) 
    {
        HashSet<char> vowels = new HashSet<char>() {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        int left = 0;
        int right = 0;
        for (int i = 0; i < s.Length; i++)
        {
            if (vowels.Contains(s[i]))
            {
                if (i < s.Length / 2)
                {
                    left += 1;
                }
                else
                {
                    right += 1;
                }
            }
        }
        return left == right;
    }
}
// @lc code=end

