/*
 * @lc app=leetcode id=1524 lang=csharp
 *
 * [1524] Number of Sub-arrays With Odd Sum
 */

// @lc code=start
public class Solution 
{
    public int NumOfSubarrays(int[] arr) 
    {
        long odd = 0;
        long even = 0; 
        int n = arr.Length;
        long result = 0;
        long MOD = 1000000007;
        for (int i = 0; i < n; i++)
        {
            long oddNew = 0;
            long evenNew = 0;
            if (arr[i] % 2 == 1)
            {
                oddNew++;
                if (i > 0)
                {
                    oddNew += even;
                    evenNew += odd;
                }
            }
            else
            {
                evenNew++;
                if (i > 0)
                {
                    oddNew += odd;
                    evenNew += even;
                }
            }
            odd = oddNew;
            even = evenNew;
            result += odd;
            result %= MOD;
        }
        return Convert.ToInt32(result);   
    }
}
// @lc code=end

