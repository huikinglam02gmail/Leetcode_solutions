/*
 * @lc app=leetcode id=2108 lang=csharp
 *
 * [2108] Find First Palindromic String in the Array
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public string FirstPalindrome(string[] words) {
        foreach (string word in words) {
            int i = 0, j = word.Length - 1;
            while (i < j && word[i] == word[j]) {
                i++;
                j--;
            }
            if (i >= j) return word;
        }
        return "";
    }
}

// @lc code=end

