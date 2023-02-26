/*
 * @lc app=leetcode id=1663 lang=csharp
 *
 * [1663] Smallest String With A Given Numeric Value
 */

// @lc code=start
using System.Text;
using System;
public class Solution 
{
    public string GetSmallestString(int n, int k) 
    {
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < n + 1; i++)
        {
            int chInd = Math.Max(1, k - 26 * (n - i));
            sb.Append(Convert.ToChar(chInd + (int)'a' - 1));
            k -= chInd;
        }  
        return sb.ToString();  
    }
}
// @lc code=end

