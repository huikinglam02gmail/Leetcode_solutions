/*
 * @lc app=leetcode id=2591 lang=csharp
 *
 * [2591] Distribute Money to Maximum Children
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    private Dictionary<Tuple<int, int>, int> memo = new Dictionary<Tuple<int, int>, int>();

    /**
     * Follow the rule
     */
    public int DistMoney(int money, int children)
    {
        if (money < children)
            return -1;

        if (children == 1)
        {
            if (money == 4)
                return -1;
            else if (money == 8)
                return 1;
            else
                return 0;
        }

        var key = Tuple.Create(money, children);

        if (memo.TryGetValue(key, out int cachedResult))
        {
            return cachedResult;
        }

        int result = 0;

        for (int i = 1; i < Math.Min(money, 9); i++)
        {
            if (i == 4)
                continue;

            int nextStep = DistMoney(money - i, children - 1);

            if (nextStep >= 0)
            {
                result = Math.Max(result, i == 8 ? 1 + nextStep : 0);
            }
        }

        memo[key] = result;
        return result;
    }
}

// @lc code=end

