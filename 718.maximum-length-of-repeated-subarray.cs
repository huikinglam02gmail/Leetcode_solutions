/*
 * @lc app=leetcode id=718 lang=csharp
 *
 * [718] Maximum Length of Repeated Subarray
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution 
{
    private long[] lookup;
    private const long basis = 101;
    private const long MOD = 1 << 31 - 1;
    private int[] nums1;
    private int[] nums2;
    public int FindLength(int[] nums1, int[] nums2) 
    {
        this.nums1 = nums1;
        this.nums2 = nums2;
        int m = nums1.Length;
        int n = nums2.Length;

        lookup = new long[Math.Min(m, n)];
        long seed = 1;
        for (int i = 0; i < Math.Min(m, n); i++)
        {
            lookup[i] = seed;
            seed *= basis;
            seed %= MOD;
        }

        int left = 1;
        int right = Math.Min(m, n) + 1;
        int result = 0;

        while (left < right) 
        {
            int mid = left + (right - left) / 2;
            if (FoundSubArray(mid)) 
            {
                left = mid + 1;
            } 
            else 
            {
                right = mid;
            }
        }

        return left - 1;
    }

    private bool FoundSubArray(int size) {

        Dictionary<long, List<int>> seen = new Dictionary<long, List<int>>();
        long h = 0;
        for (int i = 0; i < nums1.Length - size + 1; i++) 
        {
            h = RollingHash(nums1, i, size, h);
            if (!seen.ContainsKey(h)) 
            {
                seen[h] = new List<int>();
            }
            seen[h].Add(i);
        }

        h = 0;
        for (int i = 0; i < nums2.Length - size + 1; i++) 
        {
            h = RollingHash(nums2, i, size, h);
            if (seen.ContainsKey(h)) 
            {
                foreach (int j in seen[h]) 
                {
                    if (ArrayEquals(j, i, size)) 
                    {
                        return true;
                    }
                }
            }
        }

        return false;
    }

    private long RollingHash(int[] arr, int i, int size, long seed) 
    {
        long h = seed;
        if (i == 0) 
        {
            for (int j = 0; j < size; j++) 
            {
                h *= basis;
                h += arr[i + j];
                h %= MOD;
            }
        } 
        else 
        {
            h -= arr[i - 1] * lookup[size - 1];
            while (h < 0)
            {
                h += MOD;
            }               
            h %= MOD;
            h *= basis;
            h += arr[i + size - 1];
            h %= MOD;
        }
        return h;
    }

    private bool ArrayEquals(int start1, int start2, int size) 
    {
        for (int i = 0; i < size; i++) 
        {
            if (nums1[start1 + i] != nums2[start2 + i]) 
            {
                return false;
            }
        }
        return true;
    }
}

// @lc code=end

