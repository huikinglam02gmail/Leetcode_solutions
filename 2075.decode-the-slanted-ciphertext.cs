/*
 * @lc app=leetcode id=2075 lang=csharp
 *
 * [2075] Decode the Slanted Ciphertext
 */

// @lc code=start
using System;
using System.Text;

public class Solution {
    public string DecodeCiphertext(string encodedText, int rows) {
        StringBuilder result = new StringBuilder();
        int cols = encodedText.Length / rows;
        for (int i = 0; i < cols; i++) {
            int cur = i;
            while (cur < encodedText.Length) {
                result.Append(encodedText[cur]);
                cur += cols + 1;
            }
        }
        while (result.Length > 0 && result[result.Length - 1] == ' ') {
            result.Length--;
        }
        return result.ToString();
    }
}

// @lc code=end

