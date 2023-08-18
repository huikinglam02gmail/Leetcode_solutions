/*
 * @lc app=leetcode id=1855 lang=csharp
 *
 * [1855] Maximum Distance Between a Pair of Values
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
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

    public int MaxDistance(int[] nums1, int[] nums2) {
        Array.Reverse(nums1);
        Array.Reverse(nums2);
        int result = 0;
        int n1 = nums1.Length;
        int n2 = nums2.Length;
        
        for (int i1 = n1 - 1; i1 >= 0; i1--) {
            int ind = bisectLeft<int>(nums2, nums1[i1]);
            if (ind < n2 - n1 + i1 + 1) {
                result = Math.Max(result, n2 - n1 + i1 - ind);
            }
        }
        
        return result;
    }
}

// @lc code=end

