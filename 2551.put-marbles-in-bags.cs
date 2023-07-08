/*
 * @lc app=leetcode id=2551 lang=csharp
 *
 * [2551] Put Marbles in Bags
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    /*
    Find k max / min pairs of weights[0] + weights[-1] + (weights[i] + weight[i+1]), i from 0 to n - 2    
    */

    public long PutMarbles(int[] weights, int k)
    {
        if (k == 1)
        {
            return 0;
        }

        List<long> data = new List<long>();
        for (int i = 0; i < weights.Length - 1; i++)
        {
            data.Add(Convert.ToInt64(weights[i] + weights[i + 1]));
        }

        data.Sort();
        return data.GetRange(data.Count - k + 1, k - 1).Sum() - data.GetRange(0, k - 1).Sum();
    }
}

// @lc code=end

