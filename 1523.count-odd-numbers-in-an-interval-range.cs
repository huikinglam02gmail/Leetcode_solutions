/*
 * @lc app=leetcode id=1523 lang=csharp
 *
 * [1523] Count Odd Numbers in an Interval Range
 */

// @lc code=start
public class Solution 
{
    public int CountOdds(int low, int high) 
    {
        int result = (high - low) / 2;
        if (low % 2 == 1 || high % 2 == 1)
        {
            result++;
        }    
        return result;
    }
}
// @lc code=end

