/*
 * @lc app=leetcode id=1218 lang=csharp
 *
 * [1218] Longest Arithmetic Subsequence of Given Difference
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    /*
    simple DP question
    dp[i] = a hash table of length of LAS for arr[:i+1], ending with different numbers
    a new number can only contribute to 1 of them
    */
    public int LongestSubsequence(int[] arr, int difference) {
        Dictionary<int, int> dp = new Dictionary<int, int>();
        int maxSeen = 0;
        
        foreach (int num in arr) {
            dp[num] = Math.Max(dp.GetValueOrDefault(num, 0), 1 + dp.GetValueOrDefault(num - difference, 0));
            maxSeen = Math.Max(maxSeen, dp[num]);
        }
        
        return maxSeen;
    }
}



// @lc code=end

