/*
 * @lc app=leetcode id=2035 lang=csharp
 *
 * [2035] Partition Array Into Two Arrays to Minimize Sum Difference
 */

// @lc code=start
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    private List<List<int>> SubSetSums(int[] nums)
    {
        int n = nums.Length;
        List<List<int>> sums = new List<List<int>>();

        for (int i = 0; i <= n; i++)
        {
            var s = new HashSet<int>();
            foreach (var comb in Combinations(nums, i))
            {
                s.Add(comb.Sum());
            }
            sums.Add(s.OrderBy(x => x).ToList());
        }

        return sums;
    }

    public IList<IList<int>> Combinations(int[] nums, int k)
    {
        IList<IList<int>> indicesList = Combine(nums.Length, k);
        List<IList<int>> result = new List<IList<int>>();
        foreach (IList<int> indices in indicesList)
        {
            result.Add(indices.Select(x => nums[x]).ToList());
        }
        return result;
    }
    public IList<IList<int>> Combine(int n, int k) {
        var numbers = Enumerable.Range(0, n).ToList();
        var result = new List<IList<int>>();
        
        CombineHelper(numbers, k, 0, new List<int>(), result);
        return result;
    }
    
    private void CombineHelper(List<int> numbers, int k, int start, List<int> current, List<IList<int>> result) {
        if (k == 0) {
            result.Add(new List<int>(current));
            return;
        }
        
        for (int i = start; i < numbers.Count; i++) {
            current.Add(numbers[i]);
            CombineHelper(numbers, k - 1, i + 1, current, result);
            current.RemoveAt(current.Count - 1);
        }
    }

    public int MinimumDifference(int[] nums)
    {
        int n = nums.Length / 2;
        int[] left = nums.Take(n).ToArray();
        int[] right = nums.Skip(n).ToArray();

        List<List<int>> leftSums = SubSetSums(left);
        List<List<int>> rightSums = SubSetSums(right);

        int S = nums.Sum();
        int target = S / 2;
        int result = int.MaxValue;

        for (int i = 0; i <= n; i++)
        {
            foreach (int s in leftSums[i])
            {
                int ind = bisectLeft<int>(rightSums[n - i], target - s);
                if (0 <= ind && ind < rightSums[n - i].Count) result = Math.Min(result, Math.Abs(2 * (rightSums[n - i][ind] + s) - S));
                if (0 <= ind - 1 && ind - 1 < rightSums[n - i].Count) result = Math.Min(result, Math.Abs(2 * (rightSums[n - i][ind - 1] + s) - S));
                if (0 <= ind + 1 && ind + 1 < rightSums[n - i].Count) result = Math.Min(result, Math.Abs(2 * (rightSums[n - i][ind + 1] + s) - S));
            }
        }

        return result;
    }

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

}

// @lc code=end

