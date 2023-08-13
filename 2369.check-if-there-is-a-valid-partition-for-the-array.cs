/*
 * @lc app=leetcode id=2369 lang=csharp
 *
 * [2369] Check if There is a Valid Partition For The Array
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public bool ValidPartition(int[] nums) {
        bool b = false, c = true, d = true;
        int n = nums.Length;
        bool a = false;

        for (int i = 1; i < n; i++) {
            a = false;
            if (nums[i] == nums[i - 1]) {
                a |= c;
            }
            if (i > 1 && nums[i] == nums[i - 1] && nums[i] == nums[i - 2]) {
                a |= d;
            }
            if (i > 1 && nums[i] == nums[i - 1] + 1 && nums[i] == nums[i - 2] + 2) {
                a |= d;
            }
            d = c;
            c = b;
            b = a;
        }

        return a;
    }
}

// @lc code=end

