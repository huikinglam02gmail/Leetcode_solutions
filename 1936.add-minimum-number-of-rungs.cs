/*
 * @lc app=leetcode id=1936 lang=csharp
 *
 * [1936] Add Minimum Number of Rungs
 */

// @lc code=start
public class Solution 
{
    public int insertRungs(int diff, int dist)
    {
        int result = diff / dist;
        if (diff % dist == 0)
        {
            result--;
        }
        return result;
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

    public int AddRungs(int[] rungs, int dist) 
    {
        int h = 0;
        int i = -1;
        int n = rungs.Length;
        int result = 0;
        while (i < n - 1)
        {
            int ind = bisectRight<int>(rungs, h + dist);
            if (ind - 1 > i)
            {
                i = ind - 1;
            }
            else
            {
                i = ind;
                result += insertRungs(rungs[i] - h, dist);
            }
            h = rungs[i];
        }
        int diff = rungs.Last() - h;
        if (diff > 0)
        {
            result += insertRungs(diff, dist);
        }
        return result;
    }
}
// @lc code=end

