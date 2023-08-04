/*
 * @lc app=leetcode id=1838 lang=csharp
 *
 * [1838] Frequency of the Most Frequent Element
 */

// @lc code=start
public class Solution {
    public int MaxFrequency(int[] nums, int k)
    {
        Array.Sort(nums);
        List<long> prefix = new List<long> { 0 };
        foreach (int num in nums)
        {
            prefix.Add(prefix[prefix.Count - 1] + num);
        }
        int result = 0;
        int j = 0;
        int n = nums.Length;
        for (int i = 0; i < n; i++)
        {
            while ((long)(i - j) * (long)nums[i] - (long)prefix[i] + (long)prefix[j] > (long)k)
            {
                j++;
            }
            result = Math.Max(result, i + 1 - j);
        }
        return result;
    }
}
// @lc code=end

