/*
 * @lc app=leetcode id=992 lang=csharp
 *
 * [992] Subarrays with K Different Integers
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    /*
    A sliding window problem
    It is rather hard to count subarrays with exactly k different integers
    But we can tweak the question a little bit:
    number of good subarrays = number of subarray with at most k different integers - number of subarrays with at most k - 1 different integers 
    */
    public int SubarraysWithLessThanOrEqualToKDistinct(int[] nums, int k) {
        Dictionary<int, int> counter = new Dictionary<int, int>();
        int l = 0;
        int res = 0;
        for (int r = 0; r < nums.Length; r++) {
            if (!counter.ContainsKey(nums[r]))
                counter[nums[r]] = 0;
            counter[nums[r]]++;
            while (counter.Count > k) {
                counter[nums[l]]--;
                if (counter[nums[l]] == 0)
                    counter.Remove(nums[l]);
                l++;
            }
            res += r - l + 1;
        }
        return res;
    }
    
    public int SubarraysWithKDistinct(int[] nums, int k) {
        return SubarraysWithLessThanOrEqualToKDistinct(nums, k) - SubarraysWithLessThanOrEqualToKDistinct(nums, k - 1);
    }
}

// @lc code=end

