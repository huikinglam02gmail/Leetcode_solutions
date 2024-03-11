/*
 * @lc app=leetcode id=2063 lang=csharp
 *
 * [2063] Vowels of All Substrings
 */

// @lc code=start
public class Solution {
    public long CountVowels(string word) {
        long last = 0;
        long result = 0;
        int n = word.Length;
        for (int i = 0; i < n; i++) {
            if ("aeiou".Contains(word[i])) {
                last += i + 1;
            }
            result += last;
        }
        return result;
    }
}
// @lc code=end

