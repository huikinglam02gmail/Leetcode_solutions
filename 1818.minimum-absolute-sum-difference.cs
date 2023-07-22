/*
 * @lc app=leetcode id=1818 lang=csharp
 *
 * [1818] Minimum Absolute Sum Difference
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    /*
     * We can only replace numbers in nums1. The number to look for is the number in nums1
     * just smaller than and above nums2[i].
     */
    private static int bisectLeft<T>(IList<T> arr, T x, int lo=0, int hi=-1) where T : IConvertible, IComparable, IComparable<T>, IEquatable<T>
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
    public int MinAbsoluteSumDiff(int[] nums1, int[] nums2)
    {
        const long MOD = 1000000007;
        int[] nums1Sorted = new int[nums1.Length];
        Array.Copy(nums1, nums1Sorted, nums1.Length);
        Array.Sort(nums1Sorted);

        long result = nums1.Zip(nums2, (first, second) => Convert.ToInt64(Math.Abs(first - second))).Sum();
        long maxGain = 0;
        for (int i = 0; i < nums2.Length; i++)
        {
            int num = nums2[i];
            int indLeft = bisectLeft(nums1Sorted, num);
            int gain = Math.Abs(nums1[i] - num);
            if (indLeft > 0 && indLeft <= nums1Sorted.Length)
                gain = Math.Min(gain, Math.Abs(nums1Sorted[indLeft - 1] - num));
            if (indLeft >= 0 && indLeft < nums1Sorted.Length)
                gain = Math.Min(gain, Math.Abs(nums1Sorted[indLeft] - num));

            maxGain = Math.Max(maxGain, Convert.ToInt64(Math.Abs(nums1[i] - num) - gain));
        }
        return Convert.ToInt32((result - maxGain) % MOD);
    }
}

// @lc code=end

