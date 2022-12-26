/*
 * @lc app=leetcode id=55 lang=csharp
 *
 * [55] Jump Game
 */

// @lc code=start
public class Solution 
{
    public bool CanJump(int[] nums) 
    {
        int n = nums.Length;
        int position = n - 1;
        for (int i = n - 2; i >= 0; i--)
        {
            if (i + nums[i] >= position)
            {
                position = i;
            }
        }    
        return position == 0;
    }
}
// @lc code=end

