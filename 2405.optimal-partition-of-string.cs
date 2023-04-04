/*
 * @lc app=leetcode id=2405 lang=csharp
 *
 * [2405] Optimal Partition of String
 */

// @lc code=start
using System.Collections.Generic;
public class Solution 
{
    public int PartitionString(string s) 
    {
        HashSet<char> current = new HashSet<char>();
        int result = 0;
        foreach (char c in s)
        {
            if (current.Contains(c))
            {
                result++;
                current.Clear();
            }
            current.Add(c);
        }
        return result + 1;
    }
}
// @lc code=end

