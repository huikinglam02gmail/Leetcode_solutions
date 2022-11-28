/*
 * @lc app=leetcode id=1498 lang=csharp
 *
 * [1498] Number of Subsequences That Satisfy the Given Sum Condition
 */

// @lc code=start
public class Solution 
{
    public int bisectRight(int[] nums, int target)
    {
        int n = nums.Length;
        int left = 0;
        int right = n;
        while (left < right)
        {
            int mid = (left + right) / 2;
            if (nums[mid] > target)
            {
                right = mid;
            }
            else
            {
                left = mid + 1;
            }
        }
        return left;
    }
    public int NumSubseq(int[] nums, int target) 
    {
        long MOD = 1000000007;
        int n = nums.Length;
        long result = 0;
        long[] pow2 = new long[n];

        for (int i = 0; i < n; i++)
        {
            if (i == 0)
            {
                pow2[i] = 1;
            }
            else
            {
                pow2[i] = 2*pow2[i-1];
                pow2[i] %= MOD;
            }
        }    

        Array.Sort(nums);
        for (int i = 0; i < n; i++)
        {
            int j = bisectRight(nums, target - nums[i]);
            if (j - i > 0)
            {
                result += pow2[j - i - 1];
                result %= MOD;
            }
        }
        return (int) result;
    }
}
// @lc code=end

