/*
 * @lc app=leetcode id=2040 lang=csharp
 *
 * [2040] Kth Smallest Product of Two Sorted Arrays
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public long KthSmallestProduct(int[] nums1, int[] nums2, long k) {
        List<int> nums1Pos = new List<int>();
        List<int> nums1Neg = new List<int>();
        long nums1ZeroCount = 0;

        List<int> nums2Pos = new List<int>();
        List<int> nums2Neg = new List<int>();
        long nums2ZeroCount = 0;

        foreach (var num1 in nums1) {
            if (num1 > 0) {
                nums1Pos.Add(num1);
            } else if (num1 < 0) {
                nums1Neg.Add(-num1);
            } else {
                nums1ZeroCount++;
            }
        }

        foreach (var num2 in nums2) {
            if (num2 > 0) {
                nums2Pos.Add(num2);
            } else if (num2 < 0) {
                nums2Neg.Add(-num2);
            } else {
                nums2ZeroCount++;
            }
        }

        nums1Neg.Reverse();
        nums2Neg.Reverse();

        long neg = (long)nums1Neg.Count * (long)nums2Pos.Count + (long)nums1Pos.Count * (long)nums2Neg.Count;

        if (k <= neg) {
            return -CountKthSmallestProductOfFourSortedPositiveArrays(nums1Neg, nums2Pos, nums1Pos, nums2Neg, neg - k + 1);
        } else {
            k -= neg;
        }

        long zeros = ((long)nums1Neg.Count + (long)nums1Pos.Count) * nums2ZeroCount + ((long)nums2Neg.Count + (long)nums2Pos.Count) * nums1ZeroCount + nums1ZeroCount * nums2ZeroCount;

        if (k <= zeros) {
            return 0;
        } else {
            k -= zeros;
        }

        return CountKthSmallestProductOfFourSortedPositiveArrays(nums1Pos, nums2Pos, nums1Neg, nums2Neg, k);
    }

    private long CountNumberOfProductsBetweenTwoSortedPositiveArraysSmallerOrEqualToThres(List<int> arr1, List<int> arr2, long thres) {
        long count = 0;
        int j = arr2.Count - 1;
        foreach (var num in arr1) {
            while (j >= 0 && (long)num * (long)arr2[j] > thres) {
                j--;
            }
            count += j + 1;
        }
        return count;
    }

    private long CountKthSmallestProductOfFourSortedPositiveArrays(List<int> arr1, List<int> arr2, List<int> arr3, List<int> arr4, long k) {
        long l = long.MaxValue;
        long r = long.MinValue;

        if (arr1.Count > 0 && arr2.Count > 0) {
            l = Math.Min(l, (long)arr1[0] * (long)arr2[0]);
            r = Math.Max(r, (long)arr1[arr1.Count - 1] * (long)arr2[arr2.Count - 1] + 1);
        }

        if (arr3.Count > 0 && arr4.Count > 0) {
            l = Math.Min(l, (long)arr3[0] * (long)arr4[0]);
            r = Math.Max(r, (long)arr3[arr3.Count - 1] * (long)arr4[arr4.Count - 1] + 1);
        }

        while (l < r) {
            long mid = l + (r - l) / 2;

            if (CountNumberOfProductsBetweenTwoSortedPositiveArraysSmallerOrEqualToThres(arr1, arr2, mid) +
                CountNumberOfProductsBetweenTwoSortedPositiveArraysSmallerOrEqualToThres(arr3, arr4, mid) < k) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }

        return l;
    }
}

// @lc code=end

