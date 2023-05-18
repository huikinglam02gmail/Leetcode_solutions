/*
 * @lc app=leetcode id=1718 lang=csharp
 *
 * [1718] Construct the Lexicographically Largest Valid Sequence
 */

// @lc code=start
using System;
using System.Linq;
using System.Collections.Generic;
public class Solution 
{
    int[] arr;
    HashSet<int> used;
    int[] ans;

    public bool backtrack(int i)
    {
        if (i == arr.Length)
        {
            ans = arr.Select(x => x).ToArray();
            return true;
        }
        else if (arr[i] > 0)
        {
            return backtrack(i + 1);
        }
        else
        {
            for (int j = (arr.Length + 1) / 2; j > 0; j--)
            {
                if (!used.Contains(j) && (j > 1 ? i + j < arr.Length : true) && arr[i] == 0 && (j == 1 ? true : arr[i + j] == 0))
                {
                    used.Add(j);
                    arr[i] = j;
                    if (j > 1)
                    {
                        arr[i + j] = j;
                    }
                    if (backtrack(i + 1))
                    {
                        return true;
                    }
                    arr[i] = 0;
                    if (j > 1)
                    {
                        arr[i + j] = 0;
                    }
                    used.Remove(j);
                }
            }
            return false;
        }
    }

    public int[] ConstructDistancedSequence(int n) 
    {
        arr = new int[2 * n - 1];
        Array.Fill(arr, 0);
        used = new HashSet<int>();
        bool found = backtrack(0);
        return ans;
    }
}
// @lc code=end

