/*
 * @lc app=leetcode id=16 lang=csharp
 *
 * [16] 3Sum Closest
 */

// @lc code=start
using System;
using System.Collections.Generic;
using System.Linq;
public class Solution {
    public int ThreeSumClosest(int[] nums, int target) {
        Array.Sort(nums);
        int result = int.MaxValue;
        int n = nums.Length;
        
        for (int i = 0; i < n - 2; i++) {
            int S1 = nums[i] + nums[i + 1] + nums[i + 2];
            int S2 = nums[i] + nums[n - 2] + nums[n - 1];
            int[] candidates = new int[] { result, S1, S2 };
            result = candidates.OrderBy(x => Math.Abs(x - target)).First();
            
            if (S1 <= target && target <= S2) {
                int left = i + 1;
                int right = n - 1;
                
                while (left < right) {
                    int S = nums[i] + nums[left] + nums[right];
                    candidates = new int[] { result, S };
                    result = candidates.OrderBy(x => Math.Abs(x - target)).First();
                    
                    if (S == target) {
                        return target;
                    }
                    else if (S < target) {
                        left++;
                    }
                    else {
                        right--;
                    }
                }
            }
        }
        
        return result;
    }
}
// @lc code=end

