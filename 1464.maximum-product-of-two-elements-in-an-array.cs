/*
 * @lc app=leetcode id=1464 lang=csharp
 *
 * [1464] Maximum Product of Two Elements in an Array
 */

// @lc code=start
public class Solution 
{
    public int MaxProduct(int[] nums) 
    {
        Array.Sort(nums);
        return (nums[nums.Length-1] - 1)*(nums[nums.Length-2] - 1);
    }
}
// @lc code=end

