/*
 * @lc app=leetcode id=1437 lang=csharp
 *
 * [1437] Check If All 1's Are at Least Length K Places Away
 */

// @lc code=start
public class Solution {
    public bool KLengthApart(int[] nums, int k) {
        int n = nums.Length;
        int prev = - 2*n;
        for (int i = 0; i < n; i++)
        {
            if (nums[i] == 1)
            {
                if (i - prev <= k)
                {
                    return false;
                }
                prev = i;
            }
        }
        return true;
    }
}
// @lc code=end

