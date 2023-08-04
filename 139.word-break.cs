/*
 * @lc app=leetcode id=139 lang=csharp
 *
 * [139] Word Break
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    public bool WordBreak(string s, IList<string> wordDict) {
        Queue<string> q = new Queue<string>();
        HashSet<string> seen = new HashSet<string>();
        q.Enqueue(s);
        seen.Add(s);
        while (q.Count > 0) {
            s = q.Dequeue();
            foreach (string word in wordDict) {
                if (s.StartsWith(word)) {
                    string new_s = s.Substring(word.Length);
                    if (new_s == "") {
                        return true;
                    }
                    if (!seen.Contains(new_s)) {
                        q.Enqueue(new_s);
                        seen.Add(new_s);
                    }
                }
            }
        }
        return false;
    }
}

// @lc code=end

