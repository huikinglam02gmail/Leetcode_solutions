/*
 * @lc app=leetcode id=1239 lang=csharp
 *
 * [1239] Maximum Length of a Concatenated String with Unique Characters
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    /**
     * This is a DP problem
     * 1 <= arr.Length <= 16, small enough to do it semi-brute force
     * We can find all possible combinations inside arr which do not have overlapping characters
     * We use the dp list to keep all the possible used characters
     * dp[i] = all possible sets of unique characters if we use arr[0:i+1]
     */
    public int MaxLength(IList<string> arr)
    {
        int n = arr.Count;
        List<HashSet<char>> dp = new List<HashSet<char>> { new HashSet<char>() };

        foreach (string str in arr)
        {
            if (new HashSet<char>(str).Count == str.Length) // string is composed of unique characters
            {
                foreach (HashSet<char> ele in new List<HashSet<char>>(dp))
                {
                    if (ele.Overlaps(new HashSet<char>(str))) continue; // no overlap between element and the current string
                    dp.Add(new HashSet<char>(ele.Union(new HashSet<char>(str))));
                }
            }
        }

        return dp.Max(ele => ele.Count);
    }
}

// @lc code=end

