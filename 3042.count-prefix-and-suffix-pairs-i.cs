/*
 * @lc app=leetcode id=3042 lang=csharp
 *
 * [3042] Count Prefix and Suffix Pairs I
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int CountPrefixSuffixPairs(string[] words) {
        int n = words.Length;
        int result = 0;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (words[j].StartsWith(words[i]) && words[j].EndsWith(words[i])) {
                    result++;
                }
            }
        }
        return result;
    }
}

// @lc code=end

