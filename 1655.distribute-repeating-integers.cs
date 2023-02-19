/*
 * @lc app=leetcode id=1655 lang=csharp
 *
 * [1655] Distribute Repeating Integers
 */

// @lc code=start
using System.Collections.Generic;
using System.Linq;

public class Solution 
{
    int[] Values;
    int[] maskSum;
    Dictionary<Tuple<int, int>, bool> dict = new Dictionary<Tuple<int, int>, bool>();

    public bool dfs(int i, int mask)
    {
        if (mask == 0)
        {
            return true;
        }
        if (i == Values.Length)
        {
            return false;
        }
        Tuple<int, int> t = new Tuple<int, int>(i, mask);
        if (!dict.ContainsKey(t))
        {
            int subMask = mask;
            while (subMask > 0)
            {
                if (maskSum[subMask] <= Values[i] && dfs(i + 1, subMask ^ mask))
                {
                    dict[t] = true;
                    return true;
                }
                subMask = (subMask - 1) & mask;
            }
            dict[t] = dfs(i + 1, mask);
        }
        return dict[t];
    }

    public bool CanDistribute(int[] nums, int[] quantity) 
    {
        int m = quantity.Length;
        Dictionary<int, int> counter = new Dictionary<int, int>();
        foreach (int num in nums)
        {
            if (!counter.ContainsKey(num))
            {
                counter.Add(num, 0);
            }
            counter[num]++;
        }
        Values = counter.Values.ToArray();
        maskSum = new int[1 << m];
        Array.Fill(maskSum, 0);
        for (int mask = 0; mask < (1 << m); mask++)
        {
            for (int i = 0; i < m; i++)
            {
                if (((1 << i) & mask) != 0)
                {
                    maskSum[mask] += quantity[i];
                }
            }
        }
        return dfs(0, (1 << m) - 1);
    }
}
// @lc code=end

