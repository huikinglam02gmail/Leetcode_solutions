/*
 * @lc app=leetcode id=2869 lang=csharp
 *
 * [2869] Minimum Operations to Collect Elements
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    public int MinOperations(IList<int> nums, int k) {
        HashSet<int> need = new HashSet<int>();
        int n = nums.Count;
        for (int i = 1; i <= k; i++) {
            need.Add(i);
        }
        while (nums.Count > 0 && need.Count > 0) {
            int i = nums[nums.Count - 1];
            nums.RemoveAt(nums.Count - 1);
            if (need.Contains(i)) {
                need.Remove(i);
            }
        }
        return n - nums.Count;
    }
}

// @lc code=end

