/*
 * @lc app=leetcode id=215 lang=csharp
 *
 * [215] Kth Largest Element in an Array
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    /*
    QuickSelect algorithm
    */
    public int FindKthLargest(int[] nums, int k) {
        Random random = new Random();
        int pivot = nums[random.Next(nums.Length)];
        List<int> left = new List<int>();
        List<int> mid = new List<int>();
        List<int> right = new List<int>();
        
        foreach (int x in nums) {
            if (x > pivot) {
                left.Add(x);
            } else if (x == pivot) {
                mid.Add(x);
            } else {
                right.Add(x);
            }
        }
        
        int L = left.Count;
        int M = mid.Count;
        
        if (k <= L) {
            return FindKthLargest(left.ToArray(), k);
        } else if (k > L + M) {
            return FindKthLargest(right.ToArray(), k - L - M);
        } else {
            return mid[0];
        }
    }
}

// @lc code=end

