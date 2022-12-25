/*
 * @lc app=leetcode id=2389 lang=csharp
 *
 * [2389] Longest Subsequence With Limited Sum
 */

// @lc code=start

public class Solution 
{
    public int bisectRight(List<int> nums, int target)
    {
        int left = 0;
        int right = nums.Count;
        while (left < right)
        {
            int mid = left + (right - left) / 2;

            if (nums[mid] <= target)
            {
                left = mid + 1;
            }
            else
            {
                right = mid;
            }
        }
        return left;
    }
    public int[] AnswerQueries(int[] nums, int[] queries) 
    {
        List<int> prefix = new List<int>();
        int n = queries.Length;
        int[] result = new int[n];
        Array.Sort(nums);
        prefix.Add(0);
        foreach (int num in nums)
        {
            prefix.Add(num + prefix[prefix.Count - 1]);
        }
        for (int i = 0; i < n; i++)
        {
            result[i] = bisectRight(prefix, queries[i]) - 1;
        }
        return result;
    }
}
// @lc code=end

