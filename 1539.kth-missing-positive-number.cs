/*
 * @lc app=leetcode id=1539 lang=csharp
 *
 * [1539] Kth Missing Positive Number
 */

// @lc code=start
public class Solution 
{
    public int FindKthPositive(int[] arr, int k) 
    {
        int left = 0;
        int right = arr.Length;
        while (left < right)
        {
            int mid = left + (right - left) / 2;
            if (arr[mid] - mid - 1 < k)
            {
                left = mid + 1;
            }
            else
            {
                right = mid;
            }
        }
        return left + k;
    }
}
// @lc code=end

