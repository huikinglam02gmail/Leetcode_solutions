public class Solution 
{
    int[][] pos;
    public double euclidean(double x, double y)
    {
        double distance = 0;
        foreach (int[] p in pos)
        {
            distance += Math.Sqrt((x - p[0])*(x - p[0]) + (y - p[1])*(y - p[1]));
        }
        return distance;
    }
    public double GetMinDistSum(int[][] positions) 
    {
        pos = positions;
        int n = pos.Length;
        double step = 100;
        double limit = 0.000001;
        double x = pos.Select(x => x[0]).Sum() / (double) n;
        double y = pos.Select(x => x[1]).Sum() / (double) n;
        double current = euclidean(x, y);

        while (step > limit)
        {
            double[][] nxtDistance = new double[4][];
            double[][] nxt = new double[4][];
            nxt[0] = new double[2] {x, y + step};
            nxt[1] = new double[2] {x + step, y};
            nxt[2] = new double[2] {x, y - step};
            nxt[3] = new double[2] {x - step, y};
            for (int i = 0; i < 4; i++)
            {
                nxtDistance[i] = new double[3] {euclidean(nxt[i][0], nxt[i][1]), nxt[i][0], nxt[i][1]};
            }
            nxtDistance = nxtDistance.OrderBy(x => x[0]).ToArray();
            if (current > nxtDistance[0][0])
            {
                current = nxtDistance[0][0];
                x = nxtDistance[0][1];
                y = nxtDistance[0][2];
            }
            else
            {
                step /= 2;
            }
        }
        return current;
    }
}