/*
 * @lc app=leetcode id=421 lang=csharp
 *
 * [421] Maximum XOR of Two Numbers in an Array
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int FindMaximumXOR(int[] nums) {
        int result = 0;
        int numberOfLevels = Convert.ToString(nums.Max(), 2).Length;

        for (int i = numberOfLevels - 1; i >= 0; i--) {
            HashSet<int> prefixes = new HashSet<int>();

            foreach (int num in nums) {
                prefixes.Add(num >> i);
            }

            result <<= 1;

            foreach (int prefix in prefixes) {
                if (prefixes.Contains((result + 1) ^ prefix)) {
                    result += 1;
                    break;
                }
            }
        }

        return result;
    }
}

// @lc code=end

