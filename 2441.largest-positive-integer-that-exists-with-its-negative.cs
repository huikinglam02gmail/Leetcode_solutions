/*
 * @lc app=leetcode id=2441 lang=csharp
 *
 * [2441] Largest Positive Integer That Exists With Its Negative
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int FindMaxK(int[] nums) {
        Array.Sort(nums);
        HashSet<int> numsSet = new HashSet<int>(nums);
        int p = nums.Length - 1;
        while (p >= 0 && nums[p] > 0) {
            if (numsSet.Contains(-nums[p])) return nums[p];
            p--;
        }
        return -1;
    }
}

// @lc code=end

