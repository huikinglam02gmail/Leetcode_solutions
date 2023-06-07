/*
 * @lc app=leetcode id=1744 lang=csharp
 *
 * [1744] Can You Eat Your Favorite Candy on Your Favorite Day?
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    /*
    You cannot eat any candy of type i unless you have eaten all candies of type i - 1
    So we need to eat from left to right. Otherwise candy type does not matter
    We first do the prefix sum. prefixSum[i] = number of candies that must be eaten before eating type i
    Therefore the minimum of days before starting to eat type i candy is prefixSum[i] / dC
    And the maximum number of days to finish eating type i candy is prefixSum[i + 1]
    */
    public bool[] CanEat(int[] candiesCount, int[][] queries)
    {
        List<long> prefixSum = new List<long>() { 0 };
        foreach (int candy in candiesCount)
        {
            prefixSum.Add(prefixSum[prefixSum.Count - 1] + candy);
        }

        bool[] result = new bool[queries.Length];
        for (int i = 0; i < queries.Length; i++)
        {
            int fT = queries[i][0];
            int fD = queries[i][1];
            int dC = queries[i][2];
            result[i] = prefixSum[fT] / dC <= fD && fD < prefixSum[fT + 1];
        }
        return result;
    }
}


// @lc code=end

