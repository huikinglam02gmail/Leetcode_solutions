/*
 * @lc app=leetcode id=84 lang=csharp
 *
 * [84] Largest Rectangle in Histogram
 */

// @lc code=start
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
}
// @lc code=end

