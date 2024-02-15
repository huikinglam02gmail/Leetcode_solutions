/*
 * @lc app=leetcode id=2971 lang=csharp
 *
 * [2971] Find Polygon With the Largest Perimeter
 */

// @lc code=start
using System;
using System.Linq;

public class Solution {
    public long LargestPerimeter(int[] nums) {
        Array.Sort(nums);
        int n = nums.Length;
        long[] prefix = new long[n + 1];
        
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
        
        for (int i = n - 1; i > 0; i--) {
            if (nums[i] < prefix[i]) {
                return nums[i] + prefix[i];
            }
        }
        
        return -1;
    }
}

// @lc code=end

