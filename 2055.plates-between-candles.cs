/*
 * @lc app=leetcode id=2055 lang=csharp
 *
 * [2055] Plates Between Candles
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int[] PlatesBetweenCandles(string s, int[][] queries) {
        List<int> candles = new List<int>();
        List<int> platesBeforeCandle = new List<int>();
        int plateCount = 0;

        for (int i = 0; i < s.Length; i++) {
            if (s[i] == '*') {
                plateCount++;
            } else {
                candles.Add(i);
                platesBeforeCandle.Add(plateCount);
            }
        }

        List<int> result = new List<int>();

        foreach (var query in queries) {
            int l = query[0];
            int r = query[1];

            int leftCandleIndex = bisectLeft<int>(candles, l);
            int rightCandleIndex = bisectRight<int>(candles, r) - 1;

            int current = 0;

            if (leftCandleIndex < candles.Count) {
                current -= platesBeforeCandle[leftCandleIndex];
            } else {
                current -= plateCount;
            }

            if (rightCandleIndex >= 0) {
                current += platesBeforeCandle[rightCandleIndex];
            }

            result.Add(Math.Max(current, 0));
        }

        return result.ToArray();
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

}

// @lc code=end

