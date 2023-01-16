/*
 * @lc app=leetcode id=1620 lang=csharp
 *
 * [1620] Coordinate With Maximum Network Quality
 */

// @lc code=start
public class Solution 
{
    public double euclidean(int x1, int y1, int x2, int y2)
    {
        return Math.Sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2));
    }
    public int[] BestCoordinate(int[][] towers, int radius) 
    {
        int[,] quality = new int[51,51];
        for (int i = 0; i < 51; i++)
        {
            for (int j = 0; j < 51; j++)
            {
                quality[i,j] = 0;
                foreach (int[] tower in towers)
                {
                    double d = euclidean(i, j, tower[0], tower[1]);
                    if (d <= radius)
                    {
                        quality[i,j] += (int)Math.Floor(tower[2] / (1 + d));
                    }
                }
            }
        }
        int x = 0;
        int y = 0;
        int qMax = 0;
        for (int i = 0; i < 51; i++)
        {
            for (int j = 0; j < 51; j++)
            {
                if (quality[i,j] > qMax)
                {
                    qMax = quality[i,j];
                    x = i;
                    y = j;
                }
            }
        }
        return new int[2]{x,y};
    }
}
// @lc code=end

