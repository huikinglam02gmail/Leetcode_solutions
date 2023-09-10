/*
 * @lc app=leetcode id=1894 lang=csharp
 *
 * [1894] Find the Student that Will Replace the Chalk
 */

// @lc code=start
public class Solution {
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

    public int ChalkReplacer(int[] chalk, int k) {
        List<long> prefix = new List<long>();
        prefix.Add(0);
        
        foreach (int num in chalk) {
            prefix.Add(prefix.Last() + (long)num);
        }
        
        return bisectRight<long>(prefix, (long)k % prefix.Last()) - 1;
    }
}
// @lc code=end

