/*
 * @lc app=leetcode id=2870 lang=csharp
 *
 * [2870] Minimum Number of Operations to Make Array Empty
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    /*
    All counts must be 2 * m + 3 * n
    The best strategy is to take:
    1. count // 3 rounds of the 2nd operation, and if (count - 3 * (count // 3)) % 2 == 0, add (count - 3 * (count // 3)) // 2 of the 1st operation
    2. Take (count // 3 - 1) rounds of the 2nd operation, and if (count - 3 * (count // 3 - 1)) % 2 == 0, add (count - 3 * (count // 3 - 1)) // 2 of the 1st operation
    return -1 otherwise
    */
    public int MinOperations(int[] nums)
    {
        Dictionary<int, int> counts = new Dictionary<int, int>();
        foreach (int num in nums)
        {
            if (counts.ContainsKey(num))
            {
                counts[num]++;
            }
            else
            {
                counts[num] = 1;
            }
        }

        int result = 0;
        foreach (int v in counts.Values)
        {
            if ((v - 3 * (v / 3)) % 2 == 0)
            {
                result += v / 3 + (v - 3 * (v / 3)) / 2;
            }
            else if (v / 3 > 0 && (v - 3 * ((v / 3) - 1)) % 2 == 0)
            {
                result += v / 3 - 1 + (v - 3 * ((v / 3) - 1)) / 2;
            }
            else
            {
                return -1;
            }
        }
        return result;
    }
}

// @lc code=end

