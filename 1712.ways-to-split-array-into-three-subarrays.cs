/*
 * @lc app=leetcode id=1712 lang=csharp
 *
 * [1712] Ways to Split Array Into Three Subarrays
 */

// @lc code=start
using System.Collections.Generic;
using System.Linq;
using System;
public class Solution 
{
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

    public int WaysToSplit(int[] nums) 
    {
        long MOD = 1000000007;
        int n = nums.Length;
        List<int> prefix = new List<int>() { 0 };
        long result = 0;
        foreach (int num in nums)
        {
            prefix.Add(prefix.Last() + num);
        }

        int leftRightMost = Math.Min(n - 1, bisectRight(prefix, prefix.Last() / 3));
        for (int left = 1; left < leftRightMost; left++)
        {
            result += Math.Max(0, Math.Min(n, bisectRight(prefix, (prefix.Last() + prefix[left]) / 2)) - Math.Max(left + 1, bisectLeft(prefix, 2 * prefix[left])));
            if (result > MOD)
            {
                result %= MOD;
            }
        }
        return Convert.ToInt32(result);
    }
}
// @lc code=end

