/*
 * @lc app=leetcode id=2348 lang=csharp
 *
 * [2348] Number of Zero-Filled Subarrays
 */

// @lc code=start
public class Solution 
{
    public long ZeroFilledSubarray(int[] nums) 
    {
        long left = -1;
        long right = -1;
        long result = 0;
        int prev = 1;
        for (int i = 0; i < nums.Length; i++)
        {
            if (prev != 0 && nums[i] == 0)
            {
                left = i;
            }
            else if (prev == 0 && nums[i] != 0)
            {
                right = i;
                result += (right - left) * (right - left + 1) / 2;
            }
            prev = nums[i];
        }    
        if (nums[nums.Length - 1] == 0)
        {
            right = nums.Length;
            result += (right - left) * (right - left + 1) / 2;
        }
        return result;
    }
}
// @lc code=end

