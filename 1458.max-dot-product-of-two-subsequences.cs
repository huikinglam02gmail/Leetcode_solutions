/*
 * @lc app=leetcode id=1458 lang=csharp
 *
 * [1458] Max Dot Product of Two Subsequences
 */

// @lc code=start
public class Solution {
    Dictionary<Tuple<int, int>, int> memo = new Dictionary<Tuple<int, int>, int>();
    int[] arr1;
    int[] arr2;
    public int dp(int i, int j)
    {
        Tuple<int, int> curTuple = (i, j).ToTuple();
        if (memo.ContainsKey(curTuple))
        {
            return memo[curTuple];
        }
        else
        {
            if (i == arr1.Length || j == arr2.Length)
            {
                return 0;
            }
            else
            {
                int result = arr1[i]*arr2[j] + dp(i+1, j+1);
                result = Math.Max(result, dp(i+1, j+1));
                result = Math.Max(result, dp(i+1, j));
                result = Math.Max(result, dp(i, j+1));
                memo.Add(curTuple, result);
                return result;
            }
        }
    }
    public int MaxDotProduct(int[] nums1, int[] nums2) 
    {
        int max1 = nums1.Max();
        int min1 = nums1.Min();
        int max2 = nums2.Max();
        int min2 = nums2.Min();

        if (max1 < 0 && min2 > 0)
        {
            return max1*min2;
        }
        if (max2 < 0 && min1 > 0)
        {
            return max2*min1;
        }
        arr1 = nums1;
        arr2 = nums2;
        return dp(0,0);

    }
}
// @lc code=end

