/*
 * @lc app=leetcode id=1160 lang=csharp
 *
 * [1160] Find Words That Can Be Formed by Characters
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int CountCharacters(string[] words, string chars) {
        int[] hashChars = new int[26];
        foreach (char c in chars) {
            hashChars[c - 'a']++;
        }

        int result = 0;
        foreach (string word in words) {
            int[] hashWord = new int[26];
            foreach (char c in word) {
                hashWord[c - 'a']++;
            }

            if (IsWordFormed(hashWord, hashChars)) {
                result += word.Length;
            }
        }

        return result;
    }

    private bool IsWordFormed(int[] hashWord, int[] hashChars) {
        for (int i = 0; i < 26; i++) {
            if (hashWord[i] > hashChars[i]) {
                return false;
            }
        }
        return true;
    }
}

// @lc code=end

