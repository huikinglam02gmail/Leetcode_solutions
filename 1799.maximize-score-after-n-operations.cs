/*
 * @lc app=leetcode id=1799 lang=csharp
 *
 * [1799] Maximize Score After N Operations
 */

// @lc code=start
using System.Collections.Generic;
using System;
public class Solution 
{
    int[] Nums;
    Dictionary<Tuple<int, int>, int> memo;

    public int GCD(int a, int b)
    {
        return a == 0 ? b : GCD(b % a, a);
    }

    public int dp(int mask, int round)
    {
        Tuple<int, int> t = new Tuple<int, int>(mask, round);
        if (!memo.ContainsKey(t))
        {
            int result = 0;
            if (round <= Nums.Length)
            {
                for (int i = 0; i < Nums.Length - 1; i++)
                {
                    for (int j = i + 1; j < Nums.Length; j++)
                    {
                        if ((mask & (1 << i)) == 0 && (mask & (1 << j)) == 0)
                        {
                            result = Math.Max(result, round * GCD(Nums[i], Nums[j]) + dp(mask ^ (1 << i) ^ (1 << j), round + 1));
                        }
                    }
                }
            }
            memo.Add(t, result);
            Console.WriteLine($"{mask}, {round}, {result}");        
        }
        return memo[t];
    }

    public int MaxScore(int[] nums) 
    {
        Nums = nums;
        memo = new Dictionary<Tuple<int, int>, int>();
        return dp(0, 1);
    }
}
// @lc code=end
