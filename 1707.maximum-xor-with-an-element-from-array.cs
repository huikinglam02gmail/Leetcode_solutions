/*
 * @lc app=leetcode id=1707 lang=csharp
 *
 * [1707] Maximum XOR With an Element From Array
 */

// @lc code=start
using System;
using System.Collections.Generic;
using System.Collections;
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

    public int[] MaximizeXor(int[] nums, int[][] queries) 
    {
        Array.Sort(nums);
        List<int> result = new List<int>();
        int start;
        int stop;
        int cut;
        int num;
        foreach (int[] query in queries)
        {
            start = 0;
            stop = bisectRight(nums, query[1]);
            num = 0;
            for (int i = 30; i >= 0; i--)
            {
                cut = bisectLeft(nums, num + (1 << i), start, stop);
                if (start < cut && (query[0] & (1 << i)) > 0)
                {
                    stop = cut;
                }
                else if (cut < stop)
                {
                    start = cut;
                    num += (1 << i);
                }
            }
            result.Add(start < stop ? (num ^ query[0]) : -1);
        }
        return result.ToArray();
    }
}
// @lc code=end

