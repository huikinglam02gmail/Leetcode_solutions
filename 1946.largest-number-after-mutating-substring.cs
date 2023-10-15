/*
 * @lc app=leetcode id=1946 lang=csharp
 *
 * [1946] Largest Number After Mutating Substring
 */

// @lc code=start
/**
 * @lc app=leetcode id=1946 lang=csharp
 *
 * [1946] Largest Number After Mutating Substring
 */

using System;
using System.Collections.Generic;

public class Solution {
    public string MaximumNumber(string num, int[] change) {
        char[] newNum = num.ToCharArray();
        int n = newNum.Length;

        for (int i = 0; i < n; i++) {
            int j = i;
            if (newNum[j] < (char)(change[newNum[j] - '0'] + '0')) {
                while (j < n && newNum[j] <= (char)(change[newNum[j] - '0'] + '0')) {
                    newNum[j] = (char)(change[newNum[j] - '0'] + '0');
                    j++;
                }
            }
            if (j > i) {
                return new string(newNum);
            }
        }

        return num;
    }
}

// @lc code=end

