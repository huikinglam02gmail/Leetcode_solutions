/*
 * @lc app=leetcode id=823 lang=csharp
 *
 * [823] Binary Trees With Factors
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    public int NumFactoredBinaryTrees(int[] arr)
    {
        var hashTable = new Dictionary<long, long>();
        foreach (int num in arr)
        {
            hashTable[(long)num] = 1;
        }

        List<long> keys = new List<long>(hashTable.Keys);
        keys.Sort();

        var products = new Dictionary<long, List<long[]>>();
        long MOD = 1000000007;

        for (int i = 0; i < keys.Count; i++)
        {
            for (int j = i; j < keys.Count; j++)
            {
                long product = keys[i] * keys[j];
                if (hashTable.ContainsKey(product))
                {
                    if (!products.ContainsKey(product))
                    {
                        products[product] = new List<long[]>();
                    }
                    products[product].Add(new long[] { keys[i], keys[j] });
                }
            }
        }

        long result = 0;
        foreach (long key in keys)
        {
            if (products.ContainsKey(key))
            {
                foreach (var item in products[key])
                {
                    hashTable[key] += hashTable[item[0]] * hashTable[item[1]];
                    if (item[0] != item[1])
                    {
                        hashTable[key] += hashTable[item[0]] * hashTable[item[1]];
                    }
                    hashTable[key] %= MOD;
                }
            }
            result += hashTable[key];
            result %= MOD;
        }

        return (int)result;
    }
}

// @lc code=end

