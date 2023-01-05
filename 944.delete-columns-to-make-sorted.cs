/*
 * @lc app=leetcode id=944 lang=csharp
 *
 * [944] Delete Columns to Make Sorted
 */

// @lc code=start
public class Solution 
{
    public int MinDeletionSize(string[] strs) 
    {
        int m = strs.Length;
        int n = strs[0].Length;
        int result = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m - 1; j++)
            {
                if (strs[j + 1][i] < strs[j][i])
                {
                    result++;
                    break;
                }
            }
        }
        return result;    
    }
}
// @lc code=end

