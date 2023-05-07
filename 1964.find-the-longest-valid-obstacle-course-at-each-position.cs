/*
 * @lc app=leetcode id=1964 lang=csharp
 *
 * [1964] Find the Longest Valid Obstacle Course at Each Position
 */

// @lc code=start
using System.Collections.Generic;
public class Solution 
{
    public static int bisectRight(List<int> nums, int target)
    {
        int left = 0;
        int right = nums.Count;
        while (left < right)
        {
            int mid = left + (right - left) / 2;

            if (nums[mid] <= target)
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

    public int[] LongestObstacleCourseAtEachPosition(int[] obstacles) 
    {
        List<int> stack = new List<int>();
        List<int> result = new List<int>();
        foreach (int o in obstacles)
        {
            int i = bisectRight(stack, o);
            result.Add(i + 1);
            if (i == stack.Count)
            {
                stack.Add(o);
            }
            else
            {
                stack[i] = o;
            }
        }
        return result.ToArray();
    }
}

// @lc code=end

