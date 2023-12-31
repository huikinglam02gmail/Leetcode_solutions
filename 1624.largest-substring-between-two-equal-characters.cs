/*
 * @lc app=leetcode id=1624 lang=csharp
 *
 * [1624] Largest Substring Between Two Equal Characters
 */

// @lc code=start
public class Solution {
    public int MaxLengthBetweenEqualCharacters(string s) {
        List<int>[] occur = new List<int>[26];
        for (int i = 0; i < 26; i++) {
            occur[i] = new List<int>();
        }

        for (int i = 0; i < s.Length; i++) {
            char c = s[i];
            occur[c - 'a'].Add(i);
        }

        int result = -1;

        for (int i = 0; i < 26; i++) {
            if (occur[i].Count > 0) {
                result = Math.Max(result, occur[i][occur[i].Count - 1] - occur[i][0] - 1);
            }
        }

        return result;
    }
}

// @lc code=end

