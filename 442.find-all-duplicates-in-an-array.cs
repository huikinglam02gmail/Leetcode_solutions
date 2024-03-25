/*
 * @lc app=leetcode id=442 lang=csharp
 *
 * [442] Find All Duplicates in an Array
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    /*
    Use array index as hash_key
    when you see a number i in an array, just add the array length n to the ith element
    the original number can be recovered by getting num % n
    duplicates would be added 2 times and can be easily identified by the corresponding index
    */
    public IList<int> FindDuplicates(int[] nums) {
        int n = nums.Length;
        foreach (var num in nums) nums[((num % n) + n - 1) % n] += n;
        var result = new List<int>();
        for (int i = 0; i < n; i++) {
            if (nums[i] > 2 * n) result.Add(i + 1);
        }
        return result;
    }
}

// @lc code=end

