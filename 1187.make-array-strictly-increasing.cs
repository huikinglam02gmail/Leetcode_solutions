/*
 * @lc app=leetcode id=1187 lang=csharp
 *
 * [1187] Make Array Strictly Increasing
 */

// @lc code=start
using System.Collections.Generic;
public class Solution 
{
    private Dictionary<Tuple<int, int>, int> memo;
    private int[] Arr1;
    private int[] Arr2;
    private int bisectRight<T>(IList<T> nums, T target, int left=0, int right=-1) where T : IConvertible, IComparable, IComparable<T>, IEquatable<T>
    {
        right = (right == -1) ? nums.Count : right;
        while (left < right)
        {
            int mid = left + (right - left) / 2;

            if (nums[mid].CompareTo(target) <= 0)
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

    private int dp(int i, int prev)
    {
        Tuple<int, int> t = new Tuple<int,int>(i, prev);
        if (memo.ContainsKey(t))
        {
            return memo[t];
        }
        else if (i == Arr1.Length)
        {
            return 0;
        }
        else
        {
            int result = Arr1.Length + 1;
            if (Arr1[i] > prev)
            {
                result = Math.Min(result, dp(i + 1, Arr1[i]));
            }
            int j = bisectRight<int>(Arr2, prev);
            if (j < Arr2.Length)
            {
                result = Math.Min(result, 1 + dp(i + 1, Arr2[j]));
            }
            memo.Add(t, result);
            return result;
        }
    }
    public int MakeArrayIncreasing(int[] arr1, int[] arr2) 
    {
        Arr2 = arr2;
        Array.Sort(Arr2);
        Arr1 = arr1;
        memo = new Dictionary<Tuple<int, int>, int>();
        int result = dp(0, -1);
        return result == Arr1.Length + 1 ? -1 : result; 
    }
}
// @lc code=end

