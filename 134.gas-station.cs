/*
 * @lc app=leetcode id=134 lang=csharp
 *
 * [134] Gas Station
 */

// @lc code=start
public class Solution 
{
    public int CanCompleteCircuit(int[] gas, int[] cost) 
    {
        int current = 0;
        int deficit = 0;
        int start = 0;
        for (int i = 0; i < gas.Length; i++)
        {
            current += gas[i] - cost[i];
            if (current < 0)
            {
                start = i + 1;
                deficit += current;
                current = 0;
            }
        }    
        if (current + deficit >= 0)
        {
            return start;
        }
        else
        {
            return -1;
        }
    }
}
// @lc code=end

