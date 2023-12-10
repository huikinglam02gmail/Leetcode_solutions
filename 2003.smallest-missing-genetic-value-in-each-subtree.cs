/*
 * @lc app=leetcode id=2003 lang=csharp
 *
 * [2003] Smallest Missing Genetic Value in Each Subtree
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    private bool[] seen;
    private List<int>[] children;
    private int[] nums;

    private void DFS(int i) {
        if (!seen[nums[i]]) {
            seen[nums[i]] = true;
            foreach (int c in children[i]) {
                DFS(c);
            }
        }
    }

    public int[] SmallestMissingValueSubtree(int[] parents, int[] nums) {
        int n = parents.Length;
        int[] result = new int[n];
        seen = new bool[100001];
        Array.Fill(seen, false);
        Array.Fill(result, 1);
        seen[0] = true;
        children = new List<int>[n];
        this.nums = nums;

        for (int i = 0; i < n; i++) {
            children[i] = new List<int>();
        }

        if (Array.IndexOf(nums, 1) != -1) {
            int miss = 0;
            for (int i = 0; i < n; i++) {
                if (parents[i] != -1) {
                    children[parents[i]].Add(i);
                }
            }

            int j = Array.IndexOf(nums, 1);
            while (j != -1) {
                DFS(j);
                while (miss < 100001 && seen[miss]) {
                    miss++;
                }
                result[j] = miss;
                j = parents[j];
            }
        }

        return result;
    }
}

// @lc code=end

