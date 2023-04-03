/*
 * @lc app=leetcode id=881 lang=csharp
 *
 * [881] Boats to Save People
 */

// @lc code=start
using System;
public class Solution 
{
    public int NumRescueBoats(int[] people, int limit) 
    {
        Array.Sort(people);
        int result = 0;
        int left = 0;
        int right = people.Length - 1;
        while (left <= right)
        {
            result++;
            if (people[left] + people[right] <= limit)
            {
                left++;
            }
            right--;
        }
        return result;
    }
}
// @lc code=end

