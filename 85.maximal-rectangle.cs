/*
 * @lc app=leetcode id=85 lang=csharp
 *
 * [85] Maximal Rectangle
 */

// @lc code=start
using System.Collections.Generic;
using System;
public class Solution 
{
    public int LargestRectangleArea(int[] heights) 
    {
        int[] modifiedHeights = new int[heights.Length + 2];
        Array.Copy(heights, 0, modifiedHeights, 1, heights.Length);
        modifiedHeights[0] = 0;
        modifiedHeights[modifiedHeights.Length - 1] = 0;

        Stack<int[]> stack = new Stack<int[]>();
        int maxArea = 0;
        int index;

        for (int i = 0; i < modifiedHeights.Length; i++)
        {
            index = i;

            while (stack.TryPeek(out int[] lastElement) && lastElement[1] > modifiedHeights[i])
            {
                int[] popped = stack.Pop();
                index = popped[0];
                int height = popped[1];
                int width = i - index;
                int area = height * width;
                maxArea = Math.Max(maxArea, area);
            }

            stack.Push(new int[] { index, modifiedHeights[i] });
        }

        return maxArea;
    }

    public int MaximalRectangle(char[][] matrix)
    {
        int rows = matrix.Length;
        if (rows == 0) return 0;
        int cols = matrix[0].Length;

        int[,] numbers = new int[rows, cols];
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                numbers[i, j] = Convert.ToInt32(matrix[i][j].ToString());
            }
        }

        int maxArea = 0;
        int[] row = new int[cols];
        for (int i = 0; i < rows; i++)
        {
            if (i == 0)
            {
                for (int j = 0; j < cols; j++)
                {
                    row[j] = numbers[i, j];
                }
            }
            else
            {
                for (int j = 0; j < cols; j++)
                {
                    if (numbers[i, j] == 0)
                    {
                        row[j] = 0;
                    }
                    else
                    {
                        row[j] += numbers[i, j];
                    }
                }
            }
            maxArea = Math.Max(maxArea, LargestRectangleArea(row));
        }

        return maxArea;
    }
}
// @lc code=end

