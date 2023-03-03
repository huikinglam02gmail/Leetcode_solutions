/*
 * @lc app=leetcode id=1665 lang=csharp
 *
 * [1665] Minimum Initial Energy to Finish Tasks
 */

// @lc code=start
using System.Linq;
using System;
public class Solution 
{
    public int MinimumEffort(int[][] tasks) 
    {
        tasks = tasks.OrderBy(x => x[0] - x[1]).ToArray();
        int result = 0;
        int store = 0;
        foreach (int[] task in tasks)
        {
            int supply = Math.Max(0, task[1] - store);
            result += supply;
            store += supply - task[0];
        }   
        return result;
    }
}
// @lc code=end

