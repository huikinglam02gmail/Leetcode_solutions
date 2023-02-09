/*
 * @lc app=leetcode id=45 lang=csharp
 *
 * [45] Jump Game II
 */

// @lc code=start
public class Solution 
{
    public int Jump(int[] nums) 
    {  
        int left = 0;
        int right = 0;
        int jumps = 0;

        while (right < nums.Length - 1)
        {
            jumps++;
            int nextRight = left;
            for (int i = left; i <= right; i++)
            {
                nextRight = Math.Max(nextRight, i + nums[i]);
            }
            left = right;
            right = nextRight;
        }
        return jumps;
    }
}
// @lc code=end

