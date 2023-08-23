/*
 * @lc app=leetcode id=767 lang=csharp
 *
 * [767] Reorganize String
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution 
{
    public string ReorganizeString(string s) 
    {
        int[] hashTable = new int[26];
        foreach (char c in s) {
            hashTable[c - 'a']++;
        }
        
        if (hashTable.Max() > (s.Length + 1) / 2) {
            return "";
        }
        
        heap = new PriorityQueue<char, int>();
        for (int i = 0; i < 26; i++) 
        {
            if (hashTable[i] > 0) 
            {
                heap.Enqueue((char)(i + 'a'), - hashTable[i]);
            }
        }
        
        List<char> result = new List<char>();
        while (heap.TryDequeue(out char chr1, out int negCount1)) 
        {
            negCount1++;    
            if (heap.TryDequeue(out char chr2, out int negCount2)) 
            {
                if (result.Count > 0 && result.Last() == chr1)
                {
                    result.Add(chr2);
                    negCount2++;
                }
                if (negCount2 < 0)
                {
                    heap.Enqueue(chr2, negCount2);
                }
            }            
            result.Add(chr1);
            if (negCount1 < 0)
            {
                heap.Enqueue(chr1, negCount1);
            }
        }
        
        return string.Join("", result);
    }
    
    private PriorityQueue<char, int> heap;
}
// @lc code=end

