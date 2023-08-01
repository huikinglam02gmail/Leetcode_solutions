/*
 * @lc app=leetcode id=77 lang=csharp
 *
 * [77] Combinations
 */

// @lc code=start
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<IList<int>> Combine(int n, int k) {
        var numbers = Enumerable.Range(1, n).ToList();
        var result = new List<IList<int>>();
        
        CombineHelper(numbers, k, 0, new List<int>(), result);
        return result;
    }
    
    private void CombineHelper(List<int> numbers, int k, int start, List<int> current, List<IList<int>> result) {
        if (k == 0) {
            result.Add(new List<int>(current));
            return;
        }
        
        for (int i = start; i < numbers.Count; i++) {
            current.Add(numbers[i]);
            CombineHelper(numbers, k - 1, i + 1, current, result);
            current.RemoveAt(current.Count - 1);
        }
    }
}

// @lc code=end

