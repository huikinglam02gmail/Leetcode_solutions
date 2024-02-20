/*
 * @lc app=leetcode id=2900 lang=csharp
 *
 * [2900] Longest Unequal Adjacent Groups Subsequence I
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    public IList<string> GetLongestSubsequence(string[] words, int[] groups) {
        List<List<string>> results = new List<List<string>>() { new List<string>(), new List<string>() };
        for (int i = 0; i < words.Length; i++) {
            string word = words[i];
            int group = groups[i];
            if (results[group].Count % 2 == 0) {
                results[group].Add(word);
            }
            if (results[1 - group].Count % 2 != 0) {
                results[1 - group].Add(word);
            }
        }
        return results[0].Count >= results[1].Count ? results[0] : results[1];
    }
}

// @lc code=end

