/*
 * @lc app=leetcode id=57 lang=csharp
 *
 * [57] Insert Interval
 */

// @lc code=start
public class Solution 
{
    public int bisectLeft(List<int> arr, int x)
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

    public int bisectRight(List<int> arr, int x)
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

    public int[][] Insert(int[][] intervals, int[] newInterval) 
    {
        if (intervals.Length == 0)
        {
            return new int[1][]{newInterval};
        }
        List<int> intervalStarts = new List<int>();
        List<int> intervalEnds = new List<int>();
        foreach (int[] interval in intervals)
        {
            intervalStarts.Add(interval[0]);
            intervalEnds.Add(interval[1]);
        }
        int lval = newInterval[0];
        int rval = newInterval[1];
        int ri = bisectRight(intervalStarts, newInterval[1]);
        int li = bisectLeft(intervalEnds, newInterval[0]);
        if (li < intervals.Length)
        {
            lval = Math.Min(intervals[li][0], lval);
        }
        if (ri > 0)
        {
            rval = Math.Max(intervals[ri - 1][1], rval);
        }
        List<int[]> result = new List<int[]>();
        int ind = 0;
        bool inserted = false;
        while (ind < intervals.Length)
        {
            if (ind == li && ind == ri && !inserted)
            {
                inserted = true;
                result.Add(new int[2]{lval, rval});
            }
            else if (ind < li || ind >= ri)
            {
                result.Add(intervals[ind]);
                ind++;
            }
            else
            {
                result.Add(new int[2]{lval, rval});
                inserted = true;
                ind = ri;
            }
        }
        if (ind == ri && !inserted)
        {
            inserted = true;
            result.Add(new int[2]{lval, rval});
        }
        return result.ToArray();
    }
}
// @lc code=end
