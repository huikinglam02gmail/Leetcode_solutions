/*
 * @lc app=leetcode id=1906 lang=csharp
 *
 * [1906] Minimum Absolute Difference Queries
 */

// @lc code=start
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    /*
     * 1 <= nums[i] <= 100
     * We can save indices of appearance of each nums
     * Then binary search for each query
     */
    public int[] MinDifference(int[] nums, int[][] queries) {
        Dictionary<int, List<int>> hashTable = new Dictionary<int, List<int>>();
        for (int i = 0; i < nums.Length; i++) {
            if (!hashTable.ContainsKey(nums[i])) {
                hashTable[nums[i]] = new List<int>();
            }
            hashTable[nums[i]].Add(i);
        }
        
        List<int> allNums = hashTable.Keys.OrderBy(x => x).ToList();
        List<int> result = new List<int>();
        
        foreach (var query in queries) {
            int l = query[0];
            int r = query[1];
            List<int> appeared = new List<int>();
            result.Add(int.MaxValue);
            
            foreach (var allNum in allNums) {
                int leftIndex = bisectLeft<int>(hashTable[allNum], l);
                int rightIndex = bisectRight<int>(hashTable[allNum], r);
                
                if (rightIndex - leftIndex > 0) {
                    appeared.Add(allNum);
                    if (appeared.Count > 1) {
                        result[result.Count - 1] = Math.Min(result[result.Count - 1], appeared[appeared.Count - 1] - appeared[appeared.Count - 2]);
                    }
                }
            }
            
            if (result[result.Count - 1] == int.MaxValue) {
                result[result.Count - 1] = -1;
            }
        }
        
        return result.ToArray();
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
}

// @lc code=end

