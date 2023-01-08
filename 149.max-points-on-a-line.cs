/*
 * @lc app=leetcode id=149 lang=csharp
 *
 * [149] Max Points on a Line
 */

// @lc code=start
public class Solution 
{
    public int gcd(int a, int b)
    {
        if (a < b)
        {
            int temp = a;
            a = b;
            b = temp;
        }
        if (b == 0)
        {
            return a;
        }
        else
        {
            return gcd(b, a % b);
        }
    }
    public int MaxPoints(int[][] points) 
    {
        if (points.Length == 1)
        {
            return 1;
        }
        points = points.OrderBy(x => x[0]).ThenBy(x => x[1]).ToArray();
        Dictionary<int, HashSet<Tuple<int, int>>> hashTable1 = new Dictionary<int, HashSet<Tuple<int, int>>>();
        Dictionary<Tuple<int, int, int, int>, HashSet<Tuple<int, int>>> hashTable2 = new Dictionary<Tuple<int, int, int, int>, HashSet<Tuple<int, int>>>();
        for (int i = 0; i < points.Length - 1; i++)
        {
            for (int j = i + 1; j < points.Length; j++)
            {
                int xDiff = points[j][0] - points[i][0];

                if (xDiff == 0)
                {
                    if (!hashTable1.ContainsKey(points[i][0]))
                    {
                        hashTable1.Add(points[i][0], new HashSet<Tuple<int, int>>());
                    }
                    hashTable1[points[i][0]].Add(Tuple.Create(points[i][0], points[i][1]));
                    hashTable1[points[i][0]].Add(Tuple.Create(points[j][0], points[j][1]));
                }
                else
                {
                    int yDiff = points[j][1] - points[i][1];
                    int intercept = points[i][1]*points[j][0] - points[j][1]*points[i][0];
                    Tuple<int, int> key1;
                    Tuple<int, int> key2;
                    if (yDiff < 0)
                    {
                        int factor = gcd(xDiff, - yDiff);
                        key1 = new Tuple<int, int>(-(-yDiff / factor), xDiff / factor);
                    }
                    else
                    {
                        int factor = gcd(xDiff, yDiff);
                        key1 = new Tuple<int, int>(yDiff / factor, xDiff / factor);
                    }
                    if (intercept < 0)
                    {
                        int factor = gcd(xDiff, - intercept);
                        key2 = new Tuple<int, int>(-(-intercept / factor), xDiff / factor);
                    }
                    else
                    {
                        int factor = gcd(xDiff, intercept);
                        key2 = new Tuple<int, int>(intercept / factor, xDiff / factor);
                    }
                    Tuple<int, int, int, int> key = new Tuple<int, int, int, int>(key1.Item1, key1.Item2, key2.Item1, key2.Item2);
                    if (!hashTable2.ContainsKey(key))
                    {
                        hashTable2.Add(key, new HashSet<Tuple<int, int>>());
                    }
                    hashTable2[key].Add(Tuple.Create(points[i][0], points[i][1]));
                    hashTable2[key].Add(Tuple.Create(points[j][0], points[j][1]));
                }
            }
        }

        int result = 0;
        foreach (KeyValuePair<int, HashSet<Tuple<int, int>>> kvp in hashTable1)
        {
            result = Math.Max(result, kvp.Value.Count);
        }
        foreach (KeyValuePair<Tuple<int, int, int, int>, HashSet<Tuple<int, int>>> kvp in hashTable2)
        {
            result = Math.Max(result, kvp.Value.Count);
        }
        return result;
    }
}
// @lc code=end
