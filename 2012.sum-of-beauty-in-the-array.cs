/*
 * @lc app=leetcode id=2012 lang=csharp
 *
 * [2012] Sum of Beauty in the Array
 */

// @lc code=start
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    /*
    Use two SortedSets left and right to denote left and right of each index
    Then iterate from i = 1 to n - 2
    */
    public int SumOfBeauties(int[] nums) {
        SortedSet<Tuple<int, int>> left = new SortedSet<Tuple<int, int>>();
        SortedSet<Tuple<int, int>> right = new SortedSet<Tuple<int, int>>();

        int n = nums.Length;
        int result = 0;

        for (int i = 0; i < n; i++) {
            right.Add(Tuple.Create(nums[i], i));
        }

        for (int i = 0; i < n; i++) {
            right.Remove(Tuple.Create(nums[i], i));

            if (0 < i && i < n - 1) {
                if (nums[i - 1] < nums[i] && nums[i] < nums[i + 1]) {
                    result++;
                }

                if (left.Max.Item1 < nums[i] && nums[i] < right.Min.Item1) {
                    result++;
                }
            }

            left.Add(Tuple.Create(nums[i], i));
        }

        return result;
    }
}

// @lc code=end

