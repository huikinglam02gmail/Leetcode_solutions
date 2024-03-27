/*
 * @lc app=leetcode id=3090 lang=csharp
 *
 * [3090] Maximum Length Substring With Two Occurrences
 */

// @lc code=start
public class Solution {
    public int MaximumLengthSubstring(string s) {
        int left = 0;
        int[] seen = new int[26];
        int result = 0;
        for (int right = 0; right < s.Length; right++) {
            char c = s[right];
            while (seen[c - 'a'] == 2) {
                seen[s[left] - 'a'] -= 1;
                left += 1;
            }
            seen[c - 'a'] += 1;
            result = Math.Max(result, right - left + 1);
        }
        return result;
    }
}

// @lc code=end

