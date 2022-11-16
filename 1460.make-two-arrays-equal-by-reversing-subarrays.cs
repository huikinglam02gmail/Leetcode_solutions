/*
 * @lc app=leetcode id=1460 lang=csharp
 *
 * [1460] Make Two Arrays Equal by Reversing Subarrays
 */

// @lc code=start
public class Solution {
    public bool CanBeEqual(int[] target, int[] arr) {
        Array.Sort(target);
        Array.Sort(arr);
        return Enumerable.SequenceEqual(target, arr);
    }
}
// @lc code=end

