/*
 * @lc app=leetcode id=377 lang=csharp
 *
 * [377] Combination Sum IV
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public static int bisectRight<T>(IList<T> nums, T target, int left=0, int right=-1) where T : IConvertible, IComparable, IComparable<T>, IEquatable<T>
    {
        right = (right == -1) ? nums.Count : right;
        while (left < right)
        {
            int mid = left + (right - left) / 2;

            if (nums[mid].CompareTo(target) <= 0)
            {
                left = mid + 1;
            }
            else
            {
                right = mid;
            }
        }
        return left;
    }

    public int CombinationSum4(int[] nums, int target) {
        Array.Sort(nums);
        int[] dp = new int[target + 1];
        Array.Fill(dp, 0);
        dp[0] = 1;
        
        for (int i = nums[0]; i <= target; i++) 
        {
            int limit = bisectRight<int>(nums, i);
            
            for (int j = 0; j < limit; j++) 
            {
                dp[i] += dp[i - nums[j]];
            }
        }        
        return dp[target];
    }
}

// @lc code=end

