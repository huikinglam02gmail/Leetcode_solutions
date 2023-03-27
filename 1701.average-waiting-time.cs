/*
 * @lc app=leetcode id=1701 lang=csharp
 *
 * [1701] Average Waiting Time
 */

// @lc code=start
using System;
public class Solution 
{
    public double AverageWaitingTime(int[][] customers) 
    {
        double accu = 0;
        double result = 0;
        foreach (int[] customer in customers)
        {
            if (accu < customer[0])
            {
                accu = Convert.ToDouble(customer[0]);
            }
            accu += Convert.ToDouble(customer[1]);
            result += accu - customer[0];
        }    
        return result / Convert.ToDouble(customers.Length);
    }
}
// @lc code=end

