/*
 * @lc app=leetcode id=1232 lang=csharp
 *
 * [1232] Check If It Is a Straight Line
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    public bool CheckStraightLine(int[][] coordinates)
    {
        for (int i = 1; i < coordinates.Length - 1; i++)
        {
            if ((coordinates[i][0] - coordinates[i - 1][0]) * (coordinates[i + 1][1] - coordinates[i][1]) != (coordinates[i][1] - coordinates[i - 1][1]) * (coordinates[i + 1][0] - coordinates[i][0]))
            {
                return false;
            }
        }
        return true;
    }
}

// @lc code=end

