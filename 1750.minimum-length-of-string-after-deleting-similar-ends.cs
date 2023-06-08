/*
 * @lc app=leetcode id=1750 lang=csharp
 *
 * [1750] Minimum Length of String After Deleting Similar Ends
 */

// @lc code=start
public class Solution
{
    /*
    Remove characters from two ends by two pointer
    */
    public int MinimumLength(string s)
    {
        int n = s.Length;
        int i = 0;
        int j = n - 1;
        while (i < j && s[i] == s[j])
        {
            char common = s[i];
            while (i < n && s[i] == common && i <= j)
            {
                i++;
            }
            while (j >= 0 && s[j] == common && i <= j)
            {
                j--;
            }
        }
        if (i == j)
        {
            return 1;
        }
        else
        {
            return j - i + 1;
        }
    }
}

// @lc code=end

