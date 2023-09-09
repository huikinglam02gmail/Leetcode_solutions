/*
 * @lc app=leetcode id=1889 lang=csharp
 *
 * [1889] Minimum Space Wasted From Packaging
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
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

    public int MinWastedSpace(int[] packages, int[][] boxes) {
        const int MOD = 1000000007;
        Array.Sort(packages);
        long[] prefix = new long[packages.Length + 1];

        for (int i = 0; i < packages.Length; i++) {
            prefix[i + 1] = prefix[i] + packages[i];
        }

        long result = long.MaxValue;
        foreach (int[] box in boxes) {
            Array.Sort(box);
            long current = 0;
            int prev = 0;

            foreach (int j in box) {
                int ind = bisectRight<int>(packages, j);

                current += (ind - prev) * (long)j - (prefix[ind] - prefix[prev]);
                prev = ind;
            }

            if (prev == packages.Length) {
                result = Math.Min(result, current);
            }
        }

        return result < long.MaxValue ? (int)(result % MOD) : -1;
    }
}

// @lc code=end

