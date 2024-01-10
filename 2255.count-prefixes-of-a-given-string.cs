/*
 * @lc app=leetcode id=2255 lang=csharp
 *
 * [2255] Count Prefixes of a Given String
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    public int CountPrefixes(string[] words, string s) {
        int result = 0;
        foreach (string word in words) {
            if (s.StartsWith(word)) {
                result++;
            }
        }
        return result;
    }
}

// @lc code=end

