/*
 * @lc app=leetcode id=1287 lang=csharp
 *
 * [1287] Element Appearing More Than 25% In Sorted Array
 */

// @lc code=start
public class Solution {
    public static int bisectLeft<T>(IList<T> arr, T x, int lo=0, int hi=-1) where T : IConvertible, IComparable, IComparable<T>, IEquatable<T>
    {
        hi = (hi == -1) ? arr.Count : hi;
        while (lo < hi)
        {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid].CompareTo(x) < 0)
            {
                lo = mid + 1;
            }
            else
            {
                hi = mid;
            }
        }
        return lo;     
    }

    public static int bisectRight<T>(IList<T> nums, T target, int left=0, int right=-1) where T : IConvertible, IComparable, IComparable<T>, IEquatable<T>
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

    public int FindSpecialInteger(int[] arr) {
        int n = arr.Length;
        if (n / 4 == 0) return arr[0];
        for (int i = 0; i < n; i += n / 4)
        {
            if (bisectRight<int>(arr, arr[i]) - bisectLeft<int>(arr, arr[i]) > n / 4) return arr[i];
        }
        return -1;
    }
}
// @lc code=end

