/*
 * @lc app=leetcode id=1470 lang=csharp
 *
 * [1470] Shuffle the Array
 */

// @lc code=start
public class Solution 
{
    public int[] Shuffle(int[] nums, int n) 
    {
        int[] result = new int[2*n];
        for (int i = 0; i< n; i++)
        {
            result[2*i] = nums[i];
            result[2*i+1] = nums[n+i];
        }
        return result;
    }
}
// @lc code=end

