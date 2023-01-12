/*
 * @lc app=leetcode id=1610 lang=csharp
 *
 * [1610] Maximum Number of Visible Points
 */

// @lc code=start
public class Solution 
{   
    public int bisectLeft(List<double> arr, double x)
    {
        int lo = 0;
        int hi = arr.Count;
        while (lo < hi)
        {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] < x)
            {
                lo = mid + 1;
            }
            else
            {
                hi = mid;
            }
        }
        return lo;     
    }
    
    public int bisectRight(List<double> arr, double x)
    {
        int lo = 0;
        int hi = arr.Count;
        while (lo < hi)
        {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] > x)
            {
                hi = mid;
            }
            else
            {
                lo = mid + 1;
            }
        }
        return lo;     
    }

    public int VisiblePoints(IList<IList<int>> points, int angle, IList<int> location) 
    {
        Dictionary<Tuple<int, int>, int> seen = new Dictionary<Tuple<int, int>, int>();
        List<double> relevant = new List<double>();
        int result = 0;
        int maxSoFar = 0;
        foreach (List<int> point in points)
        {
            Tuple<int, int> t = new Tuple<int, int>(point[0], point[1]);
            if (!seen.ContainsKey(t))
            {
                seen.Add(t, 0);
            }
            seen[t]++;
        }
        foreach (Tuple<int, int> t in seen.Keys)
        {
            if (t.Item1 != location[0] || t.Item2 != location[1])
            {
                double theta = Math.Atan2(t.Item2 - location[1], t.Item1 - location[0]);
                for (int j = 0; j < seen[t]; j++)
                {
                    relevant.Add(theta);
                    relevant.Add(theta + 2*Math.PI);
                }
            }
            else
            {
                result += seen[t];
            }
        }
        if (relevant.Count > 0)
        {
            relevant.Sort();
            int ind = 0;
            while (relevant[ind] < Math.PI)
            {
                maxSoFar = Math.Max(maxSoFar, bisectRight(relevant, relevant[ind] + (double)angle*Math.PI / 180) - bisectLeft(relevant, relevant[ind]));
                ind++;
            }
        }
        return result + maxSoFar;
    }
}
// @lc code=end

