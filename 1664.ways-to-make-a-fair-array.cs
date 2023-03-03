/*
 * @lc app=leetcode id=1664 lang=csharp
 *
 * [1664] Ways to Make a Fair Array
 */

// @lc code=start
using System.Collections.Generic;
public class Solution 
{
    public int WaysToMakeFair(int[] nums) 
    {
        Dictionary<int, int> prefixOdd = new Dictionary<int, int>();
        Dictionary<int, int> prefixEven = new Dictionary<int, int>();
        int result = 0;
        int n = nums.Length;
        prefixOdd.Add(-1, 0);
        prefixEven.Add(-2, 0);
        for (int i = 0; i < n; i++)
        {
            if (i % 2 == 0)
            {
                prefixEven.Add(i, prefixEven[i - 2] + nums[i]);
            }
            else
            {
                prefixOdd.Add(i, prefixOdd[i - 2] + nums[i]);                
            }
        }


        int leftEvenSum;
        int leftOddSum;
        int rightEvenSum;
        int rightOddSum;        
        for (int i = 0; i < n; i++)
        {
            if (i % 2 == 0)
            {
                leftEvenSum = prefixEven[i - 2] - prefixEven[-2];
                leftOddSum = prefixOdd[i - 1] - prefixOdd[-1];
                if (n % 2 == 0)
                {
                    rightEvenSum = prefixEven[n - 2] - prefixEven[i];
                    rightOddSum = prefixOdd[n - 1] - prefixOdd[i - 1];
                }
                else
                {
                    rightEvenSum = prefixEven[n - 1] - prefixEven[i];
                    rightOddSum = prefixOdd[n - 2] - prefixOdd[i - 1];
                }
            }
            else
            {
                leftEvenSum = prefixEven[i - 1] - prefixEven[-2];
                leftOddSum = prefixOdd[i - 2] - prefixOdd[-1];
                if (n % 2 == 0)
                {
                    rightEvenSum = prefixEven[n - 2] - prefixEven[i - 1];
                    rightOddSum = prefixOdd[n - 1] - prefixOdd[i];
                }
                else
                {
                    rightEvenSum = prefixEven[n - 1] - prefixEven[i - 1];
                    rightOddSum = prefixOdd[n - 2] - prefixOdd[i];
                }
            }
            if (leftEvenSum + rightOddSum == leftOddSum + rightEvenSum)
            {
                result++;
            }
        }
        return result;
    }
}
// @lc code=end

