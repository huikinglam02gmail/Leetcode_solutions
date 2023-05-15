/*
 * @lc app=leetcode id=1711 lang=csharp
 *
 * [1711] Count Good Meals
 */

// @lc code=start
using System.Collections.Generic;
using System;
public class Solution 
{
    public int CountPairs(int[] deliciousness) 
    {
        Dictionary<int, int> hashTable = new Dictionary<int, int>();
        foreach (int d in deliciousness)
        {
            if (!hashTable.ContainsKey(d))
            {
                hashTable.Add(d, 0);
            }
            hashTable[d]++;
        }

        long result = 0;
        foreach (int d in hashTable.Keys)
        {
            for (int i = 0; i < 22; i++)
            {
                int partner = (1 << i) - d;
                if (hashTable.ContainsKey(partner))
                {
                    result += Convert.ToInt64(hashTable[d]) * Convert.ToInt64(d == partner ? hashTable[d] - 1 : hashTable[partner]);
                }
            }
        }
        return Convert.ToInt32((result / 2) % 1000000007);
    }
}
// @lc code=end
