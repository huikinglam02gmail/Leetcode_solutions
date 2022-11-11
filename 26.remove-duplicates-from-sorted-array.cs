/*
 * @lc app=leetcode id=26 lang=csharp
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
public class Solution 
{
    public int RemoveDuplicates(int[] nums) 
    {
        int left = 1;
        int n = nums.Length;
        for (int right = 1; right < n; right++)
        {
            if (nums[left - 1] < nums[right])
            {
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
                left += 1;
            }
        }
        return left;
    }
}
// @lc code=end

