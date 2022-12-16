/*
 * @lc app=leetcode id=1537 lang=csharp
 *
 * [1537] Get the Maximum Score
 */

// @lc code=start
public class Solution 
{
    public int MaxSum(int[] nums1, int[] nums2) 
    {
        int p1 = 0;
        int p2 = 0;
        int n1 = nums1.Length;
        int n2 = nums2.Length;
        long MOD = 1000000007;
        long[] current = new long[2] {0, 0};
        while (p1 < n2 && p2 < n2)
        {
            if (nums1[p1] < nums2[p2])
            {
                current[0] += nums1[p1];
                p1++;
            }
            else if (nums1[p1] > nums2[p2])
            {
                current[1] += nums2[p2];
                p2++;
            }
            else
            {
                long currentMax = Math.Max(current[0], current[1]);
                Array.Fill(current, currentMax + nums1[p1]);
                p1++;
                p2++;
            }
        }
        while (p1 < n1)
        {
            current[0] += nums1[p1];
            p1++;
        }
        while (p2 < n2)
        {
            current[1] += nums2[p2];
            p2++;
        }
        return Convert.ToInt32(current.Max(x => x) % MOD);
    }
}
// @lc code=end

