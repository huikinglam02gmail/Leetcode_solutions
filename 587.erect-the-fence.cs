/*
 * @lc app=leetcode id=587 lang=csharp
 *
 * [587] Erect the Fence
 */

// @lc code=start

public class Solution 
{
    public int cross(int[] o, int[] a, int[] b)
    {
        return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0]);
    }
    public int[][] OuterTrees(int[][] trees) 
    {
        List<int[]> lower = new List<int[]>();
        List<int[]> upper = new List<int[]>();
        HashSet<Tuple<int, int>> boundary = new HashSet<Tuple<int, int>>();
        int [][] result;
        if (trees.Length == 1)
        {
            return trees;
        }

        int[][] treeSorted = trees.OrderBy(x => x[0]).ThenBy(x => x[1]).ToArray();
        foreach (int[] p in treeSorted)
        {
            while (lower.Count >= 2 && cross(lower[lower.Count-2], lower[lower.Count-1], p) < 0)
            {
                lower.RemoveAt(lower.Count-1);
            }
            lower.Add(p);
        }

        Array.Reverse(treeSorted);
        foreach (int[] p in treeSorted)
        {
            while (upper.Count >= 2 && cross(upper[upper.Count-2], upper[upper.Count-1], p) < 0)
            {
                upper.RemoveAt(upper.Count-1);
            }
            upper.Add(p);
        }

        foreach (int[] p in lower)
        {
            boundary.Add(new Tuple<int, int>(p[0],p[1]));
        }
        foreach (int[] p in upper)
        {
            boundary.Add(new Tuple<int, int>(p[0],p[1]));
        }

        int n = boundary.Count;
        result = new int[n][];
        int counter = 0;

        foreach (Tuple<int, int> item in boundary)
        {
            result[counter] = new int[2];
            result[counter][0] = item.Item1;
            result[counter][1] = item.Item2;
            counter++;
        }
        return result;
    }
}
// @lc code=end

