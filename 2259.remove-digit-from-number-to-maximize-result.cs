/*
 * @lc app=leetcode id=2259 lang=csharp
 *
 * [2259] Remove Digit From Number to Maximize Result
 */

// @lc code=start
public class Solution {
    public string RemoveDigit(string number, char digit) {
        string result = "";
        int n = number.Length;
        for (int i = 0; i < n; i++) {
            if (number[i] == digit) {
                result = result.CompareTo(number.Substring(0, i) + number.Substring(i + 1)) > 0
                    ? result
                    : number.Substring(0, i) + number.Substring(i + 1);
            }
        }
        return result;
    }
}

// @lc code=end

