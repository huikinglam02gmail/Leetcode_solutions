/*
 * @lc app=leetcode id=1491 lang=csharp
 *
 * [1491] Average Salary Excluding the Minimum and Maximum Salary
 */

// @lc code=start
using System;
using System.Linq;
public class Solution 
{
    public double Average(int[] salary) 
    {
        Array.Sort(salary);
        return Convert.ToDouble(salary.Sum() - salary.First() - salary.Last()) / Convert.ToDouble(salary.Length - 2);
    }
}
// @lc code=end

