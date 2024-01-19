/*
 * @lc app=leetcode id=2540 lang=csharp
 *
 * [2540] Minimum Common Value
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    /**
     * Basically two pointers:
     * i, j on nums1, nums2
     * If nums1[i] < nums2[j]: i++
     * ElseIf nums1[i] > nums2[j]: j++
     * Else return nums1[i]
     */
    public int GetCommon(int[] nums1, int[] nums2) {
        int i = 0, j = 0;
        while (i < nums1.Length && j < nums2.Length) {
            if (nums1[i] < nums2[j]) {
                i++;
            } else if (nums1[i] > nums2[j]) {
                j++;
            } else {
                return nums1[i];
            }
        }
        return -1;
    }
}

// @lc code=end

