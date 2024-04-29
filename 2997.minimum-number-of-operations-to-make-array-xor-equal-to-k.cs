/*
 * @lc app=leetcode id=2997 lang=csharp
 *
 * [2997] Minimum Number of Operations to Make Array XOR Equal to K
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    /*
    break down k into binary representation
    for each num, add # of 0 and 1 bits in each slot.
    */
    public int MinOperations(int[] nums, int k) {
        int bitsToUse = Convert.ToString(k, 2).Length;
        foreach (int num in nums) {
            bitsToUse = Math.Max(bitsToUse, Convert.ToString(num, 2).Length);
        }
        int[] counts = new int[bitsToUse];
        foreach (int num in nums) {
            for (int i = 0; i < bitsToUse; i++) {
                if ((num & (1 << i)) != 0) {
                    counts[i]++;
                }
            }
        }
        int result = 0;
        int n = nums.Length;
        for (int i = 0; i < bitsToUse; i++) {
            if (((k & (1 << i)) == 0) ^ (counts[i] % 2 == 0)) {
                result++;
            }
        }
        return result;
    }
}

// @lc code=end

