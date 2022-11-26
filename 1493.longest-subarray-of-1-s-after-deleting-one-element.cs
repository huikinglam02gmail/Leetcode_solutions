/*
 * @lc app=leetcode id=1493 lang=csharp
 *
 * [1493] Longest Subarray of 1's After Deleting One Element
 */

// @lc code=start
public class Solution 
{
    public int LongestSubarray(int[] nums) 
    {
        int left = 0;
        int result = 0;
        int numZeros = 0;
        int n = nums.Length;

        for (int right = 0; right < n; right++)
        {
            if (nums[right] == 0)
            {
                numZeros++;
            }
            while (numZeros > 1)
            {
                if (nums[left] == 0)
                {
                    numZeros--;
                }
                left++;
            }
            result = Math.Max(result, right - left);
        }
        return result;
    }
}
// @lc code=end

