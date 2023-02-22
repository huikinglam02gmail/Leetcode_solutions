/*
 * @lc app=leetcode id=540 lang=csharp
 *
 * [540] Single Element in a Sorted Array
 */

// @lc code=start
public class Solution 
{
    public int[] SubArray(int[] array, int offset, int length)
    {
        int[] result = new int[length];
        Array.Copy(array, offset, result, 0, length);
        return result;
    }
    public int SingleNonDuplicate(int[] nums) 
    {
        int n = nums.Length;
        if (n == 1)
        {
            return nums[0];
        }    

        int mid = n / 2;
        if (mid > 0 && mid < n - 1 && nums[mid - 1] != nums[mid] && nums[mid] != nums[mid + 1])
        {
            return nums[mid];
        }
        else if (mid % 2 == 0)
        {
            if (nums[mid + 1] != nums[mid])
            {
                return SingleNonDuplicate(SubArray(nums, 0, mid - 1));
            }
            else
            {
                return SingleNonDuplicate(SubArray(nums, mid + 2, n - mid - 2));
            }
        }
        else
        {
            if (nums[mid + 1] != nums[mid])
            {
                return SingleNonDuplicate(SubArray(nums, mid + 1, n - mid - 1));
            }
            else
            {
                return SingleNonDuplicate(SubArray(nums, 0, mid));
            }            
        }
    }
}
// @lc code=end

