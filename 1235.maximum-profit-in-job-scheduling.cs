/*
 * @lc app=leetcode id=1235 lang=csharp
 *
 * [1235] Maximum Profit in Job Scheduling
 */

// @lc code=start
public class Solution 
{
    public int bisectLeft(int[] arr, int query)
    {
        int n = arr.Length;
        if (query > arr[n-1])
        {
            return n;
        }

        int left = 0;
        int right = n - 1;
        while (left < right)
        {
            int mid = (left + right) / 2;
            if (arr[mid] >= query)
            {
                right = mid;
            }
            else
            {
                left = mid + 1;
            }
        }
        return left;
    }
    public int JobScheduling(int[] startTime, int[] endTime, int[] profit) 
    {
        int n = profit.Length;
        int[][] jobs = new int[n][];
        int[] result = new int[n];
        int[] start = new int[n];
        Array.Fill(result, 0);

        for (int i = 0; i < n; i++)
        {
            jobs[i] = new int[3] {startTime[i], endTime[i], profit[i]};
        }

        Array.Sort(jobs, (x, y) => x[0].CompareTo(y[0]));
        for (int i = 0; i < n; i++)
        {
            start[i] = jobs[i][0];
        }        

        for (int i = n-1; i >= 0; i--)
        {
            int currentProfit = jobs[i][2];
            int index = bisectLeft(start, jobs[i][1]);
            if (index < n)
            {
                currentProfit += result[index];
            }
            if (i < n - 1)
            {
                result[i] = result[i+1];
            }
            result[i] = Math.Max(result[i], currentProfit);
        }
        return result[0];
    }
}
// @lc code=end

