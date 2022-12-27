/*
 * @lc app=leetcode id=2279 lang=csharp
 *
 * [2279] Maximum Bags With Full Capacity of Rocks
 */

// @lc code=start
public class Solution 
{
    public int MaximumBags(int[] capacity, int[] rocks, int additionalRocks) 
    {
        int n = capacity.Length;
        long total = 0;
        int[] free = new int[n];
        for (int i = 0; i < n; i++)
        {
            free[i] = capacity[i] - rocks[i];
            total += free[i];
        }
        if (total <= additionalRocks)
        {
            return n;
        }
        else
        {
            Array.Sort(free);
            int index = 0;
            while(free[index] <= additionalRocks && index < n)
            {
                additionalRocks -= free[index];
                index++;
            }
            return index;
        }
    }
}
// @lc code=end

