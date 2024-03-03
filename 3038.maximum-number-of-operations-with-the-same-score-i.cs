/*
 * @lc app=leetcode id=3038 lang=csharp
 *
 * [3038] Maximum Number of Operations With the Same Score I
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    public int MaxOperations(int[] nums) {
        int i = 0;
        int n = nums.Length;
        int result = 0;
        int constant = -1;
        while (i < n - 1) {
            if (nums[i] + nums[i + 1] != constant && constant > 0) break;
            if (constant < 0) constant = nums[i] + nums[i + 1];
            i += 2;
            result++;
        }
        return result;
    }
}

// @lc code=end

