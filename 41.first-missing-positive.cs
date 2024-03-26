/*
 * @lc app=leetcode id=41 lang=csharp
 *
 * [41] First Missing Positive
 */

// @lc code=start
using System;

public class Solution {
    /*
    First go through once, remove in num <= 0 and num > n
    Next, add n to each occurrence at the index
    Finally find the first index with # < n
    */
    public int FirstMissingPositive(int[] nums) {
        int n = nums.Length;
        for (int i = 0; i < n; i++) {
            int num = nums[i];
            if (num <= 0 || num > n) nums[i] = 0;
        }
        for (int i = 0; i < n; i++) {
            int num = nums[i];
            if (1 <= num % (2 * n) && num % (2 * n) <= n) {
                nums[num % (2 * n) - 1] += 2 * n;
            }
        }
        for (int i = 0; i < n; i++) {
            if (nums[i] / (2 * n) == 0) return i + 1;
        }
        return n + 1;
    }
}

// @lc code=end

