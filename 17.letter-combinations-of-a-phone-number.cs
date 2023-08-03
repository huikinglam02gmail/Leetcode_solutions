/*
 * @lc app=leetcode id=17 lang=csharp
 *
 * [17] Letter Combinations of a Phone Number
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    private Dictionary<char, string> hashTable = new Dictionary<char, string> {
        {'2', "abc"}, {'3', "def"}, {'4', "ghi"}, {'5', "jkl"},
        {'6', "mno"}, {'7', "pqrs"}, {'8', "tuv"}, {'9', "wxyz"}
    };

    private List<string> result = new List<string>();
    private string digits;

    private void DFS(int pos, string currentString) {
        if (pos == digits.Length) {
            if (!string.IsNullOrEmpty(currentString)) {
                result.Add(currentString);
            }
        }
        else {
            string s = hashTable[digits[pos]];
            foreach (char c in s) {
                DFS(pos + 1, currentString + c);
            }
        }
    }

    public IList<string> LetterCombinations(string digits) {
        result.Clear();
        this.digits = digits;
        DFS(0, "");
        return result;
    }
}

// @lc code=end

