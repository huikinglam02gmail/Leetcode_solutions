/*
 * @lc app=leetcode id=1048 lang=csharp
 *
 * [1048] Longest String Chain
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    /*
    This is a variation of the LIS problem. How to convert?
    The definition of predecessor:
    wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB
    LIS condition: nums[i] < nums[j]
    Longest string chain condition: s[i] is subsequence of s[j]
    important: len(s[i]) == len(s[j]) - 1 Otherwise no need consider
    To find the latter, we reuse function written in Leetcode 392 Is Subsequence
    and Leetcode 673 Number of Longest Increasing Subsequence    
    */

    public bool IsSubsequence(string s, string t) {
        int p1 = 0, p2 = 0;
        while (p1 < s.Length && p2 < t.Length) {
            if (s[p1] == t[p2]) {
                p1++;
            }
            p2++;
        }
        return p1 == s.Length;
    }
    
    public int LongestStrChain(string[] words) {
        Array.Sort(words, (a, b) => a.Length.CompareTo(b.Length));
        int n = words.Length;
        int[] dp = new int[n];
        for (int j = n - 2; j >= 0; j--) {
            for (int k = j + 1; k < n; k++) {
                if (words[j].Length == words[k].Length - 1 && IsSubsequence(words[j], words[k])) {
                    dp[j] = Math.Max(dp[j], dp[k] + 1);
                }
            }
        }
        int maxChain = 0;
        foreach (int chainLength in dp) {
            maxChain = Math.Max(maxChain, chainLength);
        }
        return maxChain + 1;
    }
}

// @lc code=end

