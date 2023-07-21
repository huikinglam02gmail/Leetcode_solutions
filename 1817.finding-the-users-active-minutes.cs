/*
 * @lc app=leetcode id=1817 lang=csharp
 *
 * [1817] Finding the Users Active Minutes
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    /*
     * Very easy: just use a dictionary <time, hashSet>. Return the histogram of size.
     */
    public int[] FindingUsersActiveMinutes(int[][] logs, int k)
    {
        Dictionary<int, HashSet<int>> hashTable = new Dictionary<int, HashSet<int>>();
        foreach (int[] log in logs)
        {
            int id = log[0];
            int time = log[1];
            if (!hashTable.ContainsKey(id))
            {
                hashTable[id] = new HashSet<int>();
            }
            hashTable[id].Add(time);
        }

        int[] result = new int[k];
        foreach (var valueSet in hashTable.Values)
        {
            result[valueSet.Count - 1]++;
        }

        return result;
    }
}

// @lc code=end

