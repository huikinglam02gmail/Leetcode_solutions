/*
 * @lc app=leetcode id=3079 lang=csharp
 *
 * [3079] Find the Sum of Encrypted Integers
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int SumOfEncryptedInt(int[] nums) {
        int result = 0;
        foreach (int num in nums) {
            HashSet<int> numSet = new HashSet<int>();
            foreach (char c in num.ToString()) {
                numSet.Add(int.Parse(c.ToString()));
            }
            int maxDigit = 0;
            foreach (int digit in numSet) {
                maxDigit = Math.Max(maxDigit, digit);
            }
            result += int.Parse(new string(maxDigit.ToString()[0], num.ToString().Length));
        }
        return result;
    }
}

// @lc code=end

