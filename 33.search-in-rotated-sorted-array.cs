/*
 * @lc app=leetcode id=33 lang=csharp
 *
 * [33] Search in Rotated Sorted Array
 */

// @lc code=start
using System;

public class Solution
{
    public int FindMin(int[] nums)
    {
        int l = 0;
        int r = nums.Length;
        while (l < r - 1)
        {
            int mid = l + (r - l) / 2;
            if (nums[mid] > nums[l])
            {
                l = mid;
            }
            else
            {
                r = mid;
            }
        }
        return (l + 1) % nums.Length;
    }

    public int Search(int[] nums, int target)
    {
        if (nums[0] == target)
        {
            return 0;
        }
        else if (nums[nums.Length - 1] == target)
        {
            return nums.Length - 1;
        }
        else
        {
            int ind = FindMin(nums);
            int result;
            if (ind > 0 && nums[0] < target)
            {
                result = bisectLeft(nums, target, 0, ind);               
            }
            else
            {
                result = bisectLeft(nums, target, ind, -1);
            }
            return (result == nums.Length || nums[result] != target) ? -1 : result;
        }
    }

    public static int bisectLeft<T>(IList<T> arr, T x, int lo=0, int hi=-1) where T : IConvertible, IComparable, IComparable<T>, IEquatable<T>
    {
        hi = (hi == -1) ? arr.Count : hi;
        while (lo < hi)
        {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid].CompareTo(x) < 0)
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
}


// @lc code=end

