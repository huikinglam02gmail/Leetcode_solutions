/*
 * @lc app=leetcode id=347 lang=csharp
 *
 * [347] Top K Frequent Elements
 */

// @lc code=start
using System.Collections.Generic;
using System.Linq;
using System;

public class Solution
{
    public int[] TopKFrequent(int[] nums, int k) 
    {
        Dictionary<int, int> hashTable = new Dictionary<int, int>();
        foreach (int num in nums)
        {
            if (!hashTable.ContainsKey(num))
            {
                hashTable[num] = 0;
            }
            hashTable[num]++;
        }
        
        List<int>[] freq = new List<int>[nums.Length];
        freq = freq.Select(x => new List<int>()).ToArray();
        
        foreach (KeyValuePair<int, int> kvp in hashTable)
        {
            freq[kvp.Value - 1].Add(kvp.Key);
        }
        
        List<int> result = new List<int>();
        int count = 0;
        
        for (int i = freq.Length - 1; i >= 0; i--)
        {
            if (freq[i].Count > 0)
            {
                int j = 0;
                while (count < k && j < freq[i].Count)
                {
                    result.Add(freq[i][j]);
                    j++;
                    count++;
                }
            }
        }
        
        return result.ToArray();
    }
}
// @lc code=end

