/*
 * @lc app=leetcode id=704 lang=csharp
 *
 * [704] Binary Search
 */

// @lc code=start
using System.Collections.Generic;
using System;
public class Solution 
{
    public static int bisectLeft(int[] arr, int x)
    {
        int lo = 0;
        int hi = arr.Length;
        while (lo < hi)
        {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] < x)
            {
                lo = mid + 1;
            }
            else
            {
                hi = mid;
            }
        }
        return lo;     
    }
    public int Search(int[] nums, int target) 
    {
        int index = bisectLeft(nums, target);
        return index == nums.Length || nums[index] != target ? -1 : index;
    }
}
// @lc code=end

