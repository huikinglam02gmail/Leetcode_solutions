/*
 * @lc app=leetcode id=520 lang=csharp
 *
 * [520] Detect Capital
 */

// @lc code=start
public class Solution {
    public bool DetectCapitalUse(string word) {
        return word.All(c => char.IsUpper(c)) || word.All(c => char.IsLower(c)) || (char.IsUpper(word[0]) && word.Substring(1).All(c => char.IsLower(c)));
    }
}
// @lc code=end

