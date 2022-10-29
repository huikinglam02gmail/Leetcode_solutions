/*
 * @lc app=leetcode id=1 lang=csharp
 *
 * [1] Two Sum
 */

// @lc code=start
public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        List<Tuple<int, int>> data = new List<Tuple<int, int>>();
        for (int i = 0; i < nums.Length; i++)
        {
            data.Add(new Tuple<int, int>(nums[i], i));
        }
        data.Sort();
        int l = 0;
        int r = data.Count - 1;
        int[] result = {-1,-1};
        while (l < r)
        {
            if (data[l].Item1 + data[r].Item1 == target)
            {
                result[0] = data[l].Item2;
                result[1] = data[r].Item2;
                return result;
            }
            else if (data[l].Item1 + data[r].Item1 < target)
            {
                l += 1;
            } 
            else
            {
                r -= 1;
            }                
        }
        return result;       
    }
}
// @lc code=end

