/*
 * @lc app=leetcode id=2899 lang=csharp
 *
 * [2899] Last Visited Integers
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    public int[] LastVisitedIntegers(int[] nums) {
        int k = 0;
        List<int> seen = new List<int>();
        List<int> ans = new List<int>();
        foreach (int num in nums) {
            if (num > 0) {
                seen.Add(num);
                k = 0;
            } else {
                k++;
                int n = seen.Count;
                if (k <= n) {
                    ans.Add(seen[n - k]);
                } else {
                    ans.Add(num);
                }
            }
        }
        return ans.ToArray();
    }
}

// @lc code=end

