/*
 * @lc app=leetcode id=2009 lang=csharp
 *
 * [2009] Minimum Number of Operations to Make Array Continuous
 */

// @lc code=start
using System;
using System.Collections.Generic;
using System.Linq;

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

    public int MinOperations(int[] nums) {
        int n = nums.Length;
        var distinctNums = nums.Distinct().OrderBy(x => x).ToArray();
        int result = int.MaxValue;

        foreach (var num in distinctNums) {
            int startIndex = bisectLeft<int>(distinctNums, num);
            int endIndex = bisectLeft<int>(distinctNums, num + n - 1);

            if (endIndex == distinctNums.Length || distinctNums[endIndex] != num + n - 1)
            {
                endIndex--;
            }

            result = Math.Min(result, n - (endIndex - startIndex + 1));
        }

        return result;
    }
}

// @lc code=end

