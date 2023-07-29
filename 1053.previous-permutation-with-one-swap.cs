/*
 * @lc app=leetcode id=1053 lang=csharp
 *
 * [1053] Previous Permutation With One Swap
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    /*
     * To find the previous permutation (with one swap), follow this algorithm:
     * Find the largest index i such that arr[i] > arr[i+1], for 0 <= i < n-1.
     * If the i found is -1, return arr (it means the array is already in the first permutation).
     * Find the largest index j such that j > i and arr[j] < arr[i].
     * Swap arr[i] and arr[j].
     * Return arr.
     */
    public int[] PrevPermOpt1(int[] arr)
    {
        int n = arr.Length;
        int i = n - 2;
        while (i >= 0 && arr[i] <= arr[i + 1])
        {
            i--;
        }
        if (i >= 0)
        {
            int j = n - 1;
            while (j > i && arr[i] <= arr[j])
            {
                j--;
            }
            while (j > 0 && arr[j - 1] == arr[j])
            {
                j--;
            }
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
        return arr;
    }
}

// @lc code=end

