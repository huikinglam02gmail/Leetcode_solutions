/*
 * @lc app=leetcode id=930 lang=csharp
 *
 * [930] Binary Subarrays With Sum
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int NumSubarraysWithSum(int[] nums, int goal) {
        Func<int, int> atMost = (int S) => {
            if (S < 0) return 0;
            int res = 0, i = 0;
            for (int j = 0; j < nums.Length; j++) {
                S -= nums[j];
                while (S < 0) {
                    S += nums[i];
                    i++;
                }
                res += j - i + 1;
            }
            return res;
        };
        return atMost(goal) - atMost(goal - 1);
    }
}

// @lc code=end

