/*
 * @lc app=leetcode id=1477 lang=csharp
 *
 * [1477] Find Two Non-overlapping Sub-arrays Each With Target Sum
 */

// @lc code=start
public class Solution 
{
    public int MinSumOfLengths(int[] arr, int target) 
    {
        int n = arr.Length;
        int[] prefix = new int[n+1];
        prefix[0] = 0;
        for (int i = 0; i < n; i++)
        {
            prefix[i+1] =  prefix[i] + arr[i];
        }
    }
}
// @lc code=end

