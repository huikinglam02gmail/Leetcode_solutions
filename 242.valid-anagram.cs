/*
 * @lc app=leetcode id=242 lang=csharp
 *
 * [242] Valid Anagram
 */

// @lc code=start
public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) return false;
        
        int[] sCount = new int[26];
        int[] tCount = new int[26];

        for (int i = 0; i < s.Length; i++) {
            sCount[s[i] - 'a']++;
            tCount[t[i] - 'a']++;
        }

        for (int i = 0; i < 26; i++) {
            if (sCount[i] != tCount[i]) return false;
        }

        return true;
    }
}

// @lc code=end

