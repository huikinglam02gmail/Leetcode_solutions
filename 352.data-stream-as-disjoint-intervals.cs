/*
 * @lc app=leetcode id=352 lang=csharp
 *
 * [352] Data Stream as Disjoint Intervals
 */

// @lc code=start
public class SummaryRanges 
{

    List<int[]> intervals;
    HashSet<int> appear;

    public SummaryRanges() 
    {
        intervals = new List<int[]>();
        appear = new HashSet<int>();
    }
    
    public int bisectLeft(List<int> nums, int target)
    {
        int left = 0;
        int right = nums.Count;
        int mid;

        while (left < right)
        {
            mid = left + (right - left) / 2;
            if (nums[mid] < target)
            {
                left = mid + 1;
            }
            else
            {
                right = mid;
            }
        }
        return left;  
    }

    public void AddNum(int value) 
    {
        if (!appear.Contains(value))
        {
            appear.Add(value);
            int ind = bisectLeft(intervals.Select(x => x[0]).ToList(), value);
            if (appear.Contains(value - 1) && appear.Contains(value + 1))
            {
                intervals[ind - 1][1] = intervals[ind][1];
                intervals.RemoveAt(ind);
            }
            else if (appear.Contains(value - 1))
            {
                intervals[ind - 1][1] = value;
            }
            else if (appear.Contains(value + 1))
            {
                intervals[ind][0] = value;
            }
            else
            {
                intervals.Insert(ind, new int[2]{value, value});
            }
        }
    }
    
    public int[][] GetIntervals() 
    {
        return intervals.ToArray();
    }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges obj = new SummaryRanges();
 * obj.AddNum(value);
 * int[][] param_2 = obj.GetIntervals();
 */
// @lc code=end

