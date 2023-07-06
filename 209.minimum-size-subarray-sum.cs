/*
 * @lc app=leetcode id=209 lang=csharp
 *
 * [209] Minimum Size Subarray Sum
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
    public int MinSubArrayLen(int target, int[] nums)
    {
        List<int> prefix = new List<int>();
        prefix.Add(0);
        foreach (int num in nums)
        {
            prefix.Add(num + prefix.Last());
        }

        int result = nums.Length + 1;
        for (int i = 0; i < prefix.Count - 1; i++)
        {
            int index = bisectLeft(prefix, prefix[i] + target);
            if (index < prefix.Count)
            {
                result = Math.Min(result, index - i);
            }
        }

        return result < nums.Length + 1 ? result : 0;
    }
}
// @lc code=end

