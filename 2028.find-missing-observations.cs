/*
 * @lc app=leetcode id=2028 lang=csharp
 *
 * [2028] Find Missing Observations
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int[] MissingRolls(int[] rolls, int mean, int n) {
        int sumAns = mean * (rolls.Length + n) - rolls.Sum();
        List<int> result = new List<int>();

        if (n <= sumAns && sumAns <= 6 * n) {
            int defaultDice = sumAns / n;
            result.AddRange(new int[n]);

            for (int i = 0; i < n; i++) {
                result[i] += defaultDice;
                sumAns -= defaultDice;
            }

            int ind = 0;
            while (sumAns > 0) {
                result[ind] += 1;
                sumAns -= 1;
                ind += 1;
            }
        }

        return result.ToArray();
    }
}

// @lc code=end

