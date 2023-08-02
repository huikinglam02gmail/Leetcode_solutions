/*
 * @lc app=leetcode id=46 lang=csharp
 *
 * [46] Permutations
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> Permute(int[] nums) {
        IList<IList<int>> result = new List<IList<int>>();
        PermuteHelper(nums, new List<int>(), new HashSet<int>(), result);
        return result;
    }

    private void PermuteHelper(int[] nums, List<int> currentList, HashSet<int> usedIndexes, IList<IList<int>> result) {
        if (currentList.Count == nums.Length) {
            result.Add(new List<int>(currentList));
            return;
        }

        for (int i = 0; i < nums.Length; i++) {
            if (!usedIndexes.Contains(i)) {
                currentList.Add(nums[i]);
                usedIndexes.Add(i);
                PermuteHelper(nums, currentList, usedIndexes, result);
                usedIndexes.Remove(i);
                currentList.RemoveAt(currentList.Count - 1);
            }
        }
    }
}

// @lc code=end

