/*
 * @lc app=leetcode id=2000 lang=csharp
 *
 * [2000] Reverse Prefix of Word
 */

// @lc code=start
public class Solution {
    public string ReversePrefix(string word, char ch) {
        int i = 0;
        int n = word.Length;
        while (i < n && word[i] != ch) {
            i++;
        }
        if (i == n) {
            return word;
        }
        return new string(word.Substring(0, i + 1).Reverse().ToArray()) + word.Substring(i + 1);
    }
}

// @lc code=end

