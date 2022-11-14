/*
 * @lc app=leetcode id=1453 lang=csharp
 *
 * [1453] Maximum Number of Darts Inside of a Circular Dartboard
 */

// @lc code=start
public class Solution 
{
    public int NumPoints(int[][] darts, int r) 
    {
        int result = 0;
        int n = darts.Length;
        for (int i = 0; i < n; i++)
        {
            int x = darts[i][0];
            int y = darts[i][1];
            int maxsofar = 1;
            int current = 1;
            List<double[]> angles = new List<double[]>();
            for (int j = 0; j < n; j++)
            {
                if (i != j)
                {
                    int x1 = darts[j][0];
                    int y1 = darts[j][1];
                    double d = Math.Sqrt((x1-x)*(x1-x) + (y1-y)*(y1-y));
                    if (d <= (double) 2*r)
                    {
                        double theta = Math.Atan2((double) (x1-x), (double) (y1-y));
                        double delta = Math.Acos(d / 2 / (double) r);
                        angles.Add(new double[2] {theta - delta, 1});
                        angles.Add(new double[2] {theta + delta, -1});
                    }
                }
            }
            angles = angles.OrderBy(t => t[0]).ThenBy( t => - t[1]).ToList();

            foreach (double[] angle in angles)
            {
                current += (int) angle[1];
                maxsofar = Math.Max(maxsofar, current);
            }
            result = Math.Max(result, maxsofar);
        }
        return result;
    }
}
// @lc code=end

