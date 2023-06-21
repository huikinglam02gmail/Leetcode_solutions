/*
 * @lc app=leetcode id=2448 lang=csharp
 *
 * [2448] Minimum Cost to Make Array Equal
 */

// @lc code=start
public class Solution {
    public long MinCost(int[] nums, int[] cost) {
        int n = nums.Length;
        var data = new List<Tuple<int, int>>();
        for (int i = 0; i < n; i++)
        {
            data.Add(new Tuple<int, int>(nums[i], cost[i]));
        }
        data.Sort();
        List<long> prefix_cost = new List<long>();
        List<long> prefix_mult = new List<long>();
        prefix_cost.Add(0);
        prefix_mult.Add(0);
        foreach (var item in data)
        {
            int num = item.Item1;
            int c = item.Item2;
            prefix_cost.Add(prefix_cost[prefix_cost.Count - 1] + c);
            prefix_mult.Add(prefix_mult[prefix_mult.Count - 1] + (long)c*num);
        }
        long result = Int64.MaxValue;
        for (int i = 0; i < n; i++)
        {
            result = Math.Min(result, prefix_mult[n] - prefix_mult[i+1] - prefix_mult[i] + (data[i].Item1)*(prefix_cost[i+1] + prefix_cost[i] - prefix_cost[n]));
        }
        return result;
    }
}
// @lc code=end

