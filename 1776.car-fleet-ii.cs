/*
 * @lc app=leetcode id=1776 lang=csharp
 *
 * [1776] Car Fleet II
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    public double[] GetCollisionTimes(int[][] cars)
    {
        Stack<double[]> stack = new Stack<double[]>();
        double[] result = new double[cars.Length];
        for (int i = cars.Length - 1; i >= 0; i--)
        {
            int pos = cars[i][0];
            int speed = cars[i][1];

            while (stack.Count > 0 && (speed <= stack.Peek()[1] || (stack.Peek()[0] - pos) / (speed - stack.Peek()[1]) >= stack.Peek()[2]))
            {
                stack.Pop();
            }

            if (stack.Count == 0)
            {
                stack.Push(new double[] { pos, speed, double.PositiveInfinity });
                result[i] = -1;
            }
            else
            {
                double collisionTime = (stack.Peek()[0] - pos) / (speed - stack.Peek()[1]);
                stack.Push(new double[] { pos, speed, collisionTime });
                result[i] = collisionTime;
            }
        }
        
        return result;
    }
}

// @lc code=end

