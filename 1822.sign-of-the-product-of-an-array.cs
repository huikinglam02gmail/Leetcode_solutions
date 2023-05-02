/*
 * @lc app=leetcode id=1822 lang=csharp
 *
 * [1822] Sign of the Product of an Array
 */

// @lc code=start
public class Solution 
{
    public int ArraySign(int[] nums) 
    {
        int negatives = 0;
        foreach (int num in nums)
        {
            if (num < 0)
            {
                negatives++;
            }
            else if (num == 0)
            {
                return 0;
            }
        }
        return negatives % 2 == 0 ? 1 : -1;
    }
}
// @lc code=end

