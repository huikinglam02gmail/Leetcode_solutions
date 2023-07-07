/*
 * @lc app=leetcode id=424 lang=csharp
 *
 * [424] Longest Repeating Character Replacement
 */

// @lc code=start
public class Solution
{
    /*
    sliding window: maximize length of the window while satisfying len(window) - # of most frequent <= k 
    */
    public int CharacterReplacement(string s, int k)
    {
        int left = 0;
        int right = 0;
        int[] occur = new int[26];
        int result = 0;
        while (right < s.Length)
        {
            if (right - left - occur.Max() <= k)
            {
                result = Math.Max(result, right - left);
                occur[s[right] - 'A'] += 1;
                right += 1;
            }
            else
            {
                occur[s[left] - 'A'] -= 1;
                left += 1;
            }
        }
        if (right - left - occur.Max() <= k)
        {
            result = Math.Max(result, right - left);
        }
        return result;
    }
}
// @lc code=end

