/*
 * @lc app=leetcode id=300 lang=csharp
 *
 * [300] Longest Increasing Subsequence
 */

// @lc code=start
using System.Collections.Generic;
public class Solution 
{
    public int bisectLeft(List<int> arr, int x)
    {
        int lo = 0;
        int hi = arr.Count;
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

    public int LengthOfLIS(int[] nums) 
    {
        List<int> result = new List<int>();
        for (int i = 0; i < nums.Length; i++)
        {
            if (result.Count == 0 || nums[i] > result[result.Count - 1])
            {
                result.Add(nums[i]);
            }
            else if (nums[i] < result[result.Count - 1])
            {
                int index = bisectLeft(result, nums[i]);
                result[index] = nums[i];
            }
        }
        return result.Count;
    }
}
// @lc code=end

