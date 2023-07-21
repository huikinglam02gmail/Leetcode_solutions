/*
 * @lc app=leetcode id=673 lang=csharp
 *
 * [673] Number of Longest Increasing Subsequence
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    /*
     * Patience sort
     * Put the numbers into decks
     * paths holds the cumulative number of LIS as each new num is added onto the deck, so as I facilitate binary search
     * Check out the top of the decks, find if we can place num on top of each deck
     * Requirement: num must be smaller than top of deck
     * The top of the decks is always sorted
     * We always use the leftmost deck
     * If we see a number larger than some of the tops of the decks, we binary search the previous deck's path to look for the number of LIS between the num and top of deck
     */

    public int FindNumberOfLIS(int[] nums)
    {
        List<List<int>> decks = new List<List<int>>();
        List<int> ends_decks = new List<int>();
        List<List<int>> paths = new List<List<int>>();

        foreach (int num in nums)
        {
            int deck_idx = bisectLeft<int>(ends_decks, num);
            int n_paths = 1;

            if (deck_idx > 0)
            {
                int l = bisectRight<int>(decks[deck_idx - 1], -num);
                n_paths = paths[deck_idx - 1][^1] - paths[deck_idx - 1][l];
            }

            if (deck_idx == decks.Count)
            {
                decks.Add(new List<int> { -num });
                ends_decks.Add(num);
                paths.Add(new List<int> { 0, n_paths });
            }
            else
            {
                decks[deck_idx].Add(-num);
                ends_decks[deck_idx] = num;
                paths[deck_idx].Add(n_paths + paths[deck_idx][^1]);
            }
        }

        return paths[^1][^1];
    }

    private static int bisectLeft<T>(IList<T> arr, T x, int lo=0, int hi=-1) where T : IConvertible, IComparable, IComparable<T>, IEquatable<T>
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

    private static int bisectRight<T>(IList<T> nums, T target, int left=0, int right=-1) where T : IConvertible, IComparable, IComparable<T>, IEquatable<T>
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

