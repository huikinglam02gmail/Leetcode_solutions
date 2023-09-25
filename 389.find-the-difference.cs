/*
 * @lc app=leetcode id=389 lang=csharp
 *
 * [389] Find the Difference
 */

// @lc code=start
public class Solution {
    public char FindTheDifference(string s, string t) {
        int[] sCount = new int[26];
        int[] tCount = new int[26];
        
        foreach (char c in s) {
            sCount[c - 'a']++;
        }
        
        foreach (char c in t) {
            tCount[c - 'a']++;
        }
        
        for (int i = 0; i < 26; i++) {
            if (sCount[i] != tCount[i]) {
                return (char)(i + 'a');
            }
        }
        
        return ' ';
    }
}

// @lc code=end

