/*
 * @lc app=leetcode id=2014 lang=csharp
 *
 * [2014] Longest Subsequence Repeated k Times
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    private Dictionary<Tuple<int, string>, HashSet<string>> dp;
    /*
    Check if s is a subsequence of t
    */
    private bool IsSubsequence(string s, string t) {
        int p1 = 0, p2 = 0;
        while (p1 < s.Length && p2 < t.Length) {
            if (s[p1] == t[p2]) {
                p1++;
            }
            p2++;
        }
        return p1 == s.Length;
    }

    /*
    Given remaining available characters and number of remaining characters in possible subsequences, generate all possible subsequences
    */
    private HashSet<string> GenerateCandidates(int remainCharacters, string availableCharacters) {
        Tuple<int, string> t = new Tuple<int, string>(remainCharacters, availableCharacters);
        if (!dp.ContainsKey(t))
        {
            var result = new HashSet<string>(remainCharacters == 0 ? new[] { "" } : new HashSet<string>());
            if (remainCharacters > 0) {
                for (int i = 0; i < availableCharacters.Length; i++) {
                    if (i > 0 && availableCharacters[i] == availableCharacters[i - 1]) continue;
                    var furtherSearchSet = GenerateCandidates(remainCharacters - 1, availableCharacters.Substring(0, i) + availableCharacters.Substring(i + 1));
                    foreach (var s in furtherSearchSet) {
                        result.Add(availableCharacters[i] + s);
                    }
                }
            }
            dp.Add(t, result);            
        }
        return dp[t];
    }

    public string LongestSubsequenceRepeatedK(string s, int k) {
        var occur = new int[26];
        int n = s.Length;

        foreach (var c in s) {
            occur[c - 'a']++;
        }

        var startingString = "";
        for (int i = 25; i >= 0; i--) {
            startingString += new string((char)(i + 'a'), occur[i] / k);
        }

        dp = new Dictionary<Tuple<int, string>, HashSet<string>>();

        for (int i = Math.Min(n / k, startingString.Length); i > 0; i--) {
            var candidates = new List<string>(GenerateCandidates(i, startingString));
            candidates.Sort((a, b) => string.Compare(b, a, StringComparison.Ordinal));
            
            foreach (var cand in candidates) {
                string subseq = "";
                for (int j = 0; j < k; ++j) subseq += cand;
                if (IsSubsequence(subseq , s)) {
                    return cand;
                }
            }
        }

        return "";
    }
}

// @lc code=end

