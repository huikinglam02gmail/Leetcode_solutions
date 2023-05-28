/*
 * @lc app=leetcode id=1727 lang=csharp
 *
 * [1727] Largest Submatrix With Rearrangements
 */

// @lc code=start
using System.Linq;
using System;
using System.Collections.Generic;
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

    public int LargestSubmatrix(int[][] matrix) 
    {
        int rows = matrix.Length;
        int cols = matrix[0].Length;
        int maxArea = 0;
        int[] row = new int[cols];
        for (int i = 0; i < rows; i++)
        {
            if (i == 0)
            {
                for (int j = 0; j < cols; j++)
                {
                    row[j] = matrix[i][j];
                }
            }
            else
            {
                for (int j = 0; j < cols; j++)
                {
                    if (matrix[i][j] == 0)
                    {
                        row[j] = 0;
                    }
                    else
                    {
                        row[j] += matrix[i][j];
                    }
                }
            }
            maxArea = Math.Max(maxArea, LargestRectangleArea(row.OrderBy(x => x).ToArray()));
        }

        return maxArea;
    }
}
// @lc code=end

