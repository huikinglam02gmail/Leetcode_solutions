/*
 * @lc app=leetcode id=2231 lang=csharp
 *
 * [2231] Largest Number After Digit Swaps by Parity
 */

// @lc code=start
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int LargestInteger(int num) {
        List<int>[] parity = { new List<int>(), new List<int>() };
        List<int>[] parityDigits = { new List<int>(), new List<int>() };

        string numString = num.ToString();
        for (int i = 0; i < numString.Length; ++i)
        {
            parity[(numString[i] - '0') % 2].Add(i);
            parityDigits[(numString[i] - '0') % 2].Add((numString[i] - '0'));
        }

        foreach (var list in parityDigits)
        {
            list.Sort((a, b) => b.CompareTo(a));
        }

        char[] final = new char[numString.Length];

        for (int j = 0; j < 2; j++)
        {
            for (int i = 0; i < parity[j].Count; i++)
            {
                final[parity[j][i]] = parityDigits[j][i].ToString()[0];
            }
        }

        return int.Parse(new string(final));
    }
}

// @lc code=end

