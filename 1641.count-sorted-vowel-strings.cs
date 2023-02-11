/*
 * @lc app=leetcode id=1641 lang=csharp
 *
 * [1641] Count Sorted Vowel Strings
 */

// @lc code=start
public class Solution 
{
    public int CountVowelStrings(int n) 
    {
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) / 4 / 3 / 2;    
    }
}
// @lc code=end

