/*
 * @lc app=leetcode id=125 lang=csharp
 *
 * [125] Valid Palindrome
 */

// @lc code=start
public class Solution {
    public bool IsPalindrome(string s) {
        var sb1 = new StringBuilder();
        foreach (char c in s){
            if (Char.IsLetter(c) | Char.IsNumber(c)) {
                if (Char.IsUpper(c)) {
                    sb1.Append(Char.ToLower(c));
                }
                else {
                    sb1.Append(c);
                }
            }
        }

        string final = sb1.ToString();
        int i = 0, j = final.Length - 1;
        while (i < j) {
            if (final[i] != final[j]) {
                return false;
            }
            else {
                i++;
                j--;
            }
        }
        return true;
        }
    }
// @lc code=end

