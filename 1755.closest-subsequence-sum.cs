/*
 * @lc app=leetcode id=1755 lang=csharp
 *
 * [1755] Closest Subsequence Sum
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    private List<int> dpSumBitMaskSorted(List<int> nums) {
        int l = nums.Count;
        List<int> result = new List<int> { 0 };
        for (int i = 0; i < l; i++) {
            for (int j = (int)Math.Pow(2, i); j < Math.Pow(2, i + 1); j++) {
                result.Add(nums[i] + result[j - (int)Math.Pow(2, i)]);
            }
        }
        result.Sort();
        return result;
    }

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

    public int MinAbsDifference(int[] nums, int goal) {
        int n = nums.Length;
        if (n == 1) {
            return Math.Min(Math.Abs(nums[0] - goal), Math.Abs(goal));
        } else {
            List<int> left = new List<int>();
            List<int> right = new List<int>();
            for (int i = 0; i < n / 2; i++) {
                left.Add(nums[i]);
            }
            for (int i = n / 2; i < n; i++) {
                right.Add(nums[i]);
            }
            List<int> leftSumSorted = dpSumBitMaskSorted(left);
            List<int> rightSumSorted = dpSumBitMaskSorted(right);
            int nr = rightSumSorted.Count;
            int result = int.MaxValue;
            foreach (int i in leftSumSorted) {
                int ind = bisectLeft<int>(rightSumSorted, goal - i);
                if (ind - 1 >= 0 && ind - 1 < nr) {
                    result = Math.Min(result, Math.Abs(rightSumSorted[ind - 1] + i - goal));
                }
                if (ind >= 0 && ind < nr) {
                    result = Math.Min(result, Math.Abs(rightSumSorted[ind] + i - goal));
                }
                if (ind + 1 >= 0 && ind + 1 < nr) {
                    result = Math.Min(result, Math.Abs(rightSumSorted[ind + 1] + i - goal));
                }
            }
            return result;
        }
    }
}

// @lc code=end

