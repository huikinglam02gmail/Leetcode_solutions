/*
 * @lc app=leetcode id=1819 lang=csharp
 *
 * [1819] Number of Different Subsequences GCDs
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    /*
     * This is not a DP problem. Rather, the solution is quite brute force: we just test i in [1, max(nums)]
     * whether it is the GCD of a subsequence inside nums. To test that, simply increment x = i, 2*i,.... 
     * up till max(nums). Initialize the gcd as 0. If j * i is inside nums, For example, if nums = [4, 8, 12], 
     * we first test x = 1. We see that 4 * 1 is inside nums, and now the gcd is 4. Next we test 8 * 1 is inside nums, 
     * but the gcd of 8 with 4 is still 4. Until we reach 12, we see that gcd(12, 4) = 4 != 1, so 1 is not a subsequence gcd.
     */
    public int CountDifferentSubsequenceGCDs(int[] nums)
    {
        HashSet<int> numsSet = new HashSet<int>(nums);
        int T = nums.Max() + 1;
        int res = 0;
        for (int x = 1; x < T; x++)
        {
            int g = 0;
            for (int y = x; y < T; y += x)
            {
                if (numsSet.Contains(y))
                {
                    g = GCD(g, y);
                }
                if (g == x)
                {
                    res++;
                    break;
                }
            }
        }
        return res;
    }

    private int GCD(int a, int b)
    {
        while (b != 0)
        {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}

// @lc code=end

