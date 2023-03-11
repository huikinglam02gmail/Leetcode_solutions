/*
 * @lc app=leetcode id=1671 lang=csharp
 *
 * [1671] Minimum Number of Removals to Make Mountain Array
 */

// @lc code=start
using System.Linq;
using System.Collections.Generic;
using System;
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
    public int MinimumMountainRemovals(int[] nums) 
    {
        int n = nums.Length;
        List<int[]> forward = new List<int[]>();
        List<int[]> reverse = new List<int[]>();
        int[] dpForward = new int[n + 2];    
        int[] dpReverse = new int[n + 2];
        Array.Fill(dpForward, 0);
        Array.Fill(dpReverse, 0);

        forward.Add(new int[2] {0, 0});
        for (int i = 0; i < n; i++)
        {
            int index = bisectLeft(forward.Select(x => x[0]).ToList(), nums[i]);
            if (index == forward.Count)
            {
                dpForward[i + 1] = forward.Count;
                forward.Add(new int[2]{nums[i], i + 1});
            }
            else
            {
                dpForward[i + 1] = dpForward[forward[index - 1][1]] + 1;
                if (nums[i] < forward[index][0])
                {
                    forward[index][0] = nums[i];
                    forward[index][1] = i + 1;
                }
            } 
        }

        reverse.Add(new int[2] {0, n + 1});
        for (int i = n - 1; i >= 0; i--)
        {
            int index = bisectLeft(reverse.Select(x => x[0]).ToList(), nums[i]);
            dpReverse[i + 1] = index == reverse.Count ? reverse.Count : dpReverse[reverse[index - 1][1]] + 1;
            if (index == reverse.Count)
            {
                reverse.Add(new int[2]{nums[i], i + 1});
            }
            else if (nums[i] < reverse[index][0])
            {
                reverse[index] = new int[2]{nums[i], i + 1};
            }
        }

        int result = n;
        for (int i = 2; i < n; i++)
        {
            if (dpForward[i] > 1 && dpReverse[i] > 1)
            {
                result = Math.Min(result, n + 1 - dpForward[i] - dpReverse[i]);
            }
        }
        return result;
    }
}
// @lc code=end

