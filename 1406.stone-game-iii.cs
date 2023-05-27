/*
 * @lc app=leetcode id=1406 lang=csharp
 *
 * [1406] Stone Game III
 */

// @lc code=start
using System;
public class Solution {
    public string StoneGameIII(int[] stoneValue) {
        int n = stoneValue.Length;
        int total = stoneValue.Sum();
        // Initialize the dp arrays
        int[] dp_Alice = new int[n];
        Array.Fill(dp_Alice, Int32.MinValue);
        int[] dp_Bob = new int[n];
        Array.Fill(dp_Bob, Int32.MaxValue);
        int current;
        for (int i = n-1; i >= 0; i--)
        {
            current = 0;
            for (int j = i; j < i + 3; j++)
            {
                if (j < n)
                {
                    current += stoneValue[j];
                    if (j+1 < n)
                    {
                        dp_Alice[i] = Math.Max(dp_Alice[i], current + dp_Bob[j+1]);
                        dp_Bob[i] = Math.Min(dp_Bob[i], dp_Alice[j+1]);
                    }
                    else
                    {
                        dp_Alice[i] = Math.Max(dp_Alice[i], current);
                        dp_Bob[i] = Math.Min(dp_Bob[i], 0);                        
                    }
                }
            }
        }
        if (dp_Alice[0] == (float)total / 2)
        {
           return "Tie"; 
        }
        else if (dp_Alice[0] > (float)total / 2)
        {
            return "Alice";
        }
        else
        {
            return "Bob";
        }
    }
}
// @lc code=end

