/*
 * @lc app=leetcode id=1713 lang=csharp
 *
 * [1713] Minimum Operations to Make a Subsequence
 */

// @lc code=start
using System.Linq;
using System.Collections.Generic;
public class Solution 
{
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

    public int LengthOfLIS(int[] nums) 
    {
        List<int> result = new List<int>();
        for (int i = 0; i < nums.Length; i++)
        {
            if (result.Count == 0 || nums[i] > result.Last())
            {
                result.Add(nums[i]);
            }
            else if (nums[i] < result.Last())
            {
                int index = bisectLeft(result, nums[i]);
                result[index] = nums[i];
            }
        }
        return result.Count;
    }

    public int MinOperations(int[] target, int[] arr) 
    {
        Dictionary<int, int> hashTable = target.Select((v, i) => new { value = v, index = i }).ToDictionary(x => x.value, x => x.index);
        List<int> result = new List<int>();
        foreach (int num in arr)
        {
            if (hashTable.ContainsKey(num))
            {
                result.Add(hashTable[num]);
            }
        }
        return target.Length - LengthOfLIS(result.ToArray());
    }
}
// @lc code=end

