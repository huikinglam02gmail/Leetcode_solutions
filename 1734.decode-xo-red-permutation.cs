/*
 * @lc app=leetcode id=1734 lang=csharp
 *
 * [1734] Decode XORed Permutation
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    public int[] Decode(int[] encoded)
    {
        int total = 0;
        int n = encoded.Length + 1;
        
        for (int i = 1; i <= n; i++)
        {
            total ^= i;
        }
        
        int initial = total;
        
        for (int i = 1; i < n; i += 2)
        {
            initial ^= encoded[i];
        }
        
        int[] result = new int[n];
        result[0] = initial;
        
        for (int i = 0; i < n - 1; i++)
        {
            result[i + 1] = result[i] ^ encoded[i];
        }
        
        return result;
    }
}

// @lc code=end

