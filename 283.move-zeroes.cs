/*
 * @lc app=leetcode id=283 lang=csharp
 *
 * [283] Move Zeroes
 */

// @lc code=start
using System;

public class Solution {
    public void MoveZeroes(int[] nums) {
        /*
         * Do not return anything, modify nums in-place instead.
         */

        /*
         * Keep nums[l] != 0 and nums[r] == 0 and swap
         */
        int l = 0;
        int r = 0;
        int n = nums.Length;

        while (l < n && r < n) {
            while (l < n && nums[l] == 0) {
                l++;
            }

            while (r < n && nums[r] != 0) {
                r++;
            }

            if (l < n && r < n && r < l) {
                int temp = nums[l];
                nums[l] = nums[r];
                nums[r] = temp;
            } else {
                l++;
            }
        }
    }
}

// @lc code=end

