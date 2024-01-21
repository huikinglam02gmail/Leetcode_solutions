/*
 * @lc app=leetcode id=2553 lang=csharp
 *
 * [2553] Separate the Digits in an Array
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    public int[] SeparateDigits(int[] nums) {
        List<int> result = new List<int>();
        foreach (int num in nums) {
            foreach (char c in num.ToString()) {
                result.Add(int.Parse(c.ToString()));
            }
        }
        return result.ToArray();
    }
}

// @lc code=end

