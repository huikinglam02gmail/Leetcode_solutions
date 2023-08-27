/*
 * @lc app=leetcode id=403 lang=csharp
 *
 * [403] Frog Jump
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public bool CanCross(int[] stones) {
        Dictionary<int, int> stoneTable = new Dictionary<int, int>();
        for (int i = 0; i < stones.Length; i++) {
            stoneTable[stones[i]] = i;
        }

        List<HashSet<int>> kSet = new List<HashSet<int>>();
        for (int i = 0; i < stones.Length; i++) {
            kSet.Add(new HashSet<int>());
        }
        kSet[0].Add(0);

        for (int i = 0; i < stones.Length; i++) {
            foreach (int item in kSet[i]) {
                for (int j = -1; j <= 1; j++) {
                    if (item + j >= 1 && stoneTable.ContainsKey(stones[i] + item + j)) {
                        kSet[stoneTable[stones[i] + item + j]].Add(item + j);
                    }
                }
            }
        }

        return kSet[stones.Length - 1].Count > 0;
    }
}

// @lc code=end

