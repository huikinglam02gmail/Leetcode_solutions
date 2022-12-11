/*
 * @lc app=leetcode id=1521 lang=csharp
 *
 * [1521] Find a Value of a Mysterious Function Closest to Target
 */

// @lc code=start
public class Solution 
{
    public int ClosestToTarget(int[] arr, int target)
    {
        int result = Int32.MaxValue;
        int n = arr.Length;
        HashSet<int> seen = new HashSet<int>();
        HashSet<int> seenNew = new HashSet<int>();
        for (int i = n - 1; i >= 0; i--)
        {
            seenNew.Clear();
            seenNew.Add(arr[i]);
            result = Math.Min(result, Math.Abs(arr[i] - target));
            foreach (int j in seen)
            {
                seenNew.Add(arr[i] & j);
                result = Math.Min(result, Math.Abs((arr[i] & j) - target));
            }
            seen = new HashSet<int>(seenNew);
        }
        return result;
    }
}
// @lc code=end

