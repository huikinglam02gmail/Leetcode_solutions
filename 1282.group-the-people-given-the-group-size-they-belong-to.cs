/*
 * @lc app=leetcode id=1282 lang=csharp
 *
 * [1282] Group the People Given the Group Size They Belong To
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> GroupThePeople(int[] groupSizes) {
        List<IList<int>> result = new List<IList<int>>();
        Dictionary<int, List<int>> hashTable = new Dictionary<int, List<int>>();

        for (int i = 0; i < groupSizes.Length; i++) {
            int size = groupSizes[i];

            if (!hashTable.ContainsKey(size)) {
                hashTable[size] = new List<int>();
            }

            hashTable[size].Add(i);

            if (hashTable[size].Count == size) {
                result.Add(hashTable[size]);
                hashTable.Remove(size);
            }
        }

        return result;
    }
}

// @lc code=end

