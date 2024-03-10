/*
 * @lc app=leetcode id=349 lang=csharp
 *
 * [349] Intersection of Two Arrays
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int[] Intersection(int[] nums1, int[] nums2) {
        HashSet<int> set1 = new HashSet<int>(nums1);
        HashSet<int> set2 = new HashSet<int>(nums2);
        set1.IntersectWith(set2);
        int[] result = new int[set1.Count];
        int index = 0;
        foreach (int num in set1) {
            result[index++] = num;
        }
        return result;
    }
}

// @lc code=end

