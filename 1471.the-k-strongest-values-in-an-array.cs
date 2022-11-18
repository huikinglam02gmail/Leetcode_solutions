/*
 * @lc app=leetcode id=1471 lang=csharp
 *
 * [1471] The k Strongest Values in an Array
 */

// @lc code=start
public class Solution 
{
    public int[] GetStrongest(int[] arr, int k) 
    {
        int[] arrSorted = arr.OrderBy(num => num).ToArray();
        int n = arr.Length;
        int median = arrSorted[(n-1)/2];
        return arrSorted;
    }
}
// @lc code=end

