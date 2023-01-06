/*
 * @lc app=leetcode id=1589 lang=csharp
 *
 * [1589] Maximum Sum Obtained of Any Permutation
 */

// @lc code=start
public class Solution 
{
    public int MaxSumRangeQuery(int[] nums, int[][] requests) 
    {
        List<int[]> intervals = new List<int[]>();
        List<int[]> arr = new List<int[]>();
        List<int> prefix = new List<int>();
        int appearance = 0;
        int n = nums.Length;
        int ind = 0;
        long result = 0;
        long MOD = 1000000007;
        int[] numNew = new int[n];
        foreach (int[] req in requests)
        {
            intervals.Add(new int[2] {req[0], 1});
            intervals.Add(new int[2] {req[1] + 1, -1});
        }
        intervals.OrderBy(x => x[0]).ToList();
        for (int i = 0; i < n; i++)
        {
            while (ind < intervals.Count && intervals[ind][0] == i)
            {
                appearance += intervals[ind][1];
                ind++;
            }
            arr.Add(new int[2] {appearance, i});
        }
        arr.OrderBy(x => - x[0]).ToList();
        nums = nums.OrderBy(x => -x).ToArray();
        for (int i = 0; i < n; i++)
        {
            numNew[arr[i][1]] = nums[i];
        }
        prefix.Add(0);
        for (int i = 0; i < n; i++)
        {
            prefix.Add(prefix[prefix.Count - 1] + numNew[i]);
        }
        foreach (int[] item  in requests)
        {
            result += prefix[item[1] + 1] - prefix[item[0]];
        }
        return Convert.ToInt32(result % MOD);
    }
}
// @lc code=end

