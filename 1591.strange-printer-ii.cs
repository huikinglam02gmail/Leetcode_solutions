/*
 * @lc app=leetcode id=1591 lang=csharp
 *
 * [1591] Strange Printer II
 */

// @lc code=start
public class Solution {
    int[][] A;

    public bool formCompleteRectangle(int xmin, int xmax, int ymin, int ymax, int color)
    {
        for (int j = xmin; j <= xmax; j++)
        {
            for (int k = ymin; k <= ymax; k++)
            {
                if (A[j][k] != 0 && A[j][k] != color)
                {
                    return false;
                }
            }
        }
        for (int j = xmin; j <= xmax; j++)
        {
            for (int k = ymin; k <= ymax; k++)
            {
                A[j][k] = 0;
            }
        }
        return true;
    }

    public bool IsPrintable(int[][] targetGrid) 
    {
        int m = targetGrid.Length;
        int n = targetGrid[0].Length;
        Dictionary<int, int[]> colors = new Dictionary<int, int[]>();
        Queue<int> queue = new Queue<int>();
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (!colors.ContainsKey(targetGrid[i][j]))
                {
                    colors[targetGrid[i][j]] = new int[4]{m, n, 0, 0};
                }
                colors[targetGrid[i][j]][0] = Math.Min(colors[targetGrid[i][j]][0],i);
                colors[targetGrid[i][j]][1] = Math.Min(colors[targetGrid[i][j]][1],j);
                colors[targetGrid[i][j]][2] = Math.Max(colors[targetGrid[i][j]][2],i);
                colors[targetGrid[i][j]][3] = Math.Max(colors[targetGrid[i][j]][3],j);
            }
        }
        A = targetGrid;
        foreach (int color in colors.Keys)
        {
            queue.Enqueue(color);
        }
        while (queue.Count > 0)
        {
            int oldLength = queue.Count;
            for (int i = 0; i < oldLength; i++)
            {
                int color = queue.Dequeue();
                if (!formCompleteRectangle(colors[color][0], colors[color][2],colors[color][1], colors[color][3], color))
                {
                    queue.Enqueue(color);
                }
            }
            if (queue.Count == oldLength)
            {
                return false;
            }
        }
        return true;
    }
}
// @lc code=end

